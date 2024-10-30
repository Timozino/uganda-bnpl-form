document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('bio-data-form');
    const submitButton = document.getElementById('submit-btn');

    form.addEventListener('submit', function (event) {
        // Simple front-end validation before submission
        const firstName = document.getElementById('first_name').value.trim();
        const lastName = document.getElementById('last_name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phoneNumber = document.getElementById('phone_number').value.trim();

        // Custom validation for phone number and email
        if (!phoneNumber.startsWith("+256") || phoneNumber.length !== 13) {
             alert("Phone number must start with +256 and be 14 digits long.");
            event.preventDefault();
        }

        if (firstName === '' || lastName === '' || email === '') {
            alert("Please fill out all required fields.");
            event.preventDefault();
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const commercialFields = document.getElementById('commercial-fields');
    const productUsageDropdown = document.getElementById('product_usage');

    function toggleCommercialFields() {
        if (productUsageDropdown.value === 'C') { // If Commercial is selected
            commercialFields.style.display = 'block';
        } else {
            commercialFields.style.display = 'none';
        }
    }

    // Event listener for dropdown change
    productUsageDropdown.addEventListener('change', toggleCommercialFields);

    // Initial check on page load
    toggleCommercialFields();
});
