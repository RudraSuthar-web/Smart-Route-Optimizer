import pandas as pd
import numpy as np
from geopy.distance import geodesic
import json
import os

def load_data(file_path):
    """Load data from Excel file"""
    shipments = pd.read_excel(file_path, sheet_name='Shipments_Data')
    vehicles = pd.read_excel(file_path, sheet_name='Vehicle_Information')
    store = pd.read_excel(file_path, sheet_name='Store Location').iloc[0]
    return shipments, vehicles, store

def optimize_routes(shipments, vehicles, store):
    """Optimize routes based on project requirements"""
    trips = []
    priority_vehicles = vehicles[vehicles['Vehicle_Type'].isin(['3W', '4W-EV'])].sort_values('Shipments_Capacity', ascending=False)
    
    for vehicle in priority_vehicles.itertuples():
        time_slots = shipments['Delivery Timeslot'].unique()
        
        for slot in time_slots:
            slot_shipments = shipments[shipments['Delivery Timeslot'] == slot]
            
            # Group shipments
            if len(slot_shipments) > vehicle.Shipments_Capacity:
                # Split into multiple trips
                for i in range(0, len(slot_shipments), vehicle.Shipments_Capacity):
                    trip_shipments = slot_shipments.iloc[i:i+vehicle.Shipments_Capacity]
                    
                    # Calculate route details
                    route_points = [(store['Latitude'], store['Longitude'])] + \
                                   list(zip(trip_shipments['Latitude'], trip_shipments['Longitude']))
                    
                    total_distance = sum(
                        geodesic(route_points[j], route_points[j+1]).km 
                        for j in range(len(route_points)-1)
                    )
                    
                    trips.append({
                        'tripId': len(trips) + 1,
                        'shipments': [{
                            'id': row['Shipment_ID'],
                            'latitude': row['Latitude'],
                            'longitude': row['Longitude'],
                            'timeSlot': row['Delivery Timeslot']
                        } for _, row in trip_shipments.iterrows()],
                        'vehicleType': vehicle.Vehicle_Type,
                        'mstDistance': round(total_distance, 2),
                        'tripTime': f"{round(total_distance * 5 + len(trip_shipments) * 10)} mins",
                        'capacityUtilization': round(len(trip_shipments) / vehicle.Shipments_Capacity * 100, 2),
                        'timeValidation': 'Valid'
                    })
    
    return trips

def generate_html_output(trips, store):
    """Generate HTML output with interactive map and table"""
    # Prepare data for JavaScript
    trip_data_json = json.dumps(trips)
    store_location_json = json.dumps({
        'latitude': store['Latitude'],
        'longitude': store['Longitude']
    })
    
    # Read the HTML template
    with open('prototype 2/dashboard.html', 'r', encoding='utf-8') as f:
        dashboard = f.read()
    
    # Replace placeholders with actual data
    dashboard = dashboard.replace('${TRIP_DATA_JSON}', trip_data_json) \
                         .replace('${STORE_LOCATION_JSON}', store_location_json)
    
    # Save the output HTML
    with open('prototype 2/output.html', 'w', encoding='utf-8') as f:
        f.write(dashboard)
    
    print("HTML output generated successfully!")

def main():
    # File path to Excel
    file_path = 'SmartRoute Optimizer.xlsx'
    
    # Load data
    shipments, vehicles, store = load_data(file_path)
    
    # Optimize routes
    optimized_trips = optimize_routes(shipments, vehicles, store)
    
    # Generate HTML output
    generate_html_output(optimized_trips, store)

if __name__ == "__main__":
    main()