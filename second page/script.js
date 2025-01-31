// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.getElementById('optimizerForm');
//     const successMessage = document.getElementById('successMessage');

//     form.addEventListener('submit', function(e) {
//         e.preventDefault();
        
//         // Collect form data
//         const formData = new FormData();
        
//         // Add form fields to FormData
//         formData.append('storeLat', document.getElementById('storeLat').value);
//         formData.append('storeLong', document.getElementById('storeLong').value);
//         formData.append('travelTime', document.getElementById('travelTime').value);
//         formData.append('deliveryTime', document.getElementById('deliveryTime').value);
//         formData.append('shipmentsFile', document.getElementById('shipmentsFile').files[0]);
//         formData.append('vehicleFile', document.getElementById('vehicleFile').files[0]);

//         // Show success message
//         successMessage.style.display = 'block';

//         // Hide success message after 3 seconds
//         setTimeout(() => {
//             successMessage.style.display = 'none';
//         }, 3000);

//         // Log form data for debugging
//         console.log('Form data collected:', {
//             storeLat: formData.get('storeLat'),
//             storeLong: formData.get('storeLong'),
//             travelTime: formData.get('travelTime'),
//             deliveryTime: formData.get('deliveryTime'),
//             shipmentsFile: formData.get('shipmentsFile').name,
//             vehicleFile: formData.get('vehicleFile').name
//         });

//         // Example of how to send to backend:
//         /*
//         fetch('/api/optimize', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             console.log('Success:', data);
//             successMessage.style.display = 'block';
//             setTimeout(() => {
//                 successMessage.style.display = 'none';
//             }, 3000);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('An error occurred while processing your request.');
//         });
//         */
//     });
// });

