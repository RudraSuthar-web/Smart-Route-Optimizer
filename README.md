# SmartRoute Optimizer

A Python-based route optimization system for managing delivery shipments efficiently. The system optimizes delivery routes based on vehicle capacity, time slots, and geographical locations.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Dependencies

The following Python packages are required:

```bash
pandas>=1.3.0
numpy>=1.20.0
geopy>=2.2.0
openpyxl>=3.0.0  # For Excel file support
```

## Installation

1. Clone the repository or download the project files to your local machine.

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
SmartRoute Optimizer/
├── model.py                      # Main optimization logic
├── SmartRoute Optimizer.xlsx     # Input data file
└── prototype 2/
    ├── dashboard.html           # Dashboard template
    └── output.html             # Generated output file
```

## Input Data Format

The Excel file (`SmartRoute Optimizer.xlsx`) should contain three sheets:

1. **Shipments_Data**
   - Shipment_ID
   - Latitude
   - Longitude
   - Delivery Timeslot

2. **Vehicle_Information**
   - Vehicle_Type
   - Shipments_Capacity

3. **Store Location**
   - Latitude
   - Longitude

## Usage

1. Ensure your input Excel file is properly formatted and placed in the project root directory.

2. Run the optimization model:
```bash
python model.py
```

3. The script will generate an interactive visualization in `prototype 2/output.html`

## Output

The system generates:
- Optimized delivery routes
- Distance calculations
- Trip time estimates
- Capacity utilization metrics
- Interactive map visualization

## Notes

- The system prioritizes 3W and 4W-EV vehicle types for route optimization
- Distance calculations use the geodesic distance formula
- Trip time estimates include both travel time and delivery time
- The visualization includes an interactive map showing all delivery routes

## Troubleshooting

Common issues and solutions:

1. **Excel File Not Found**
   - Verify the Excel file is in the correct location
   - Check file permissions

2. **Missing Dependencies**
   - Run `pip install -r requirements.txt` again
   - Ensure your virtual environment is activated

3. **Geopy Installation Issues**
   - Try upgrading pip: `pip install --upgrade pip`
   - Install wheel package: `pip install wheel`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
