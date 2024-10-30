document.getElementById('billing_model').addEventListener('change', function() {
    const billingModel = this.value;
    const paygoFields = document.getElementById('paygo-fields');
    const outrightFields = document.getElementById('outright-fields');

    if (billingModel === 'Paygo') {
        paygoFields.style.display = 'block';
        outrightFields.style.display = 'none';
    } else if (billingModel === 'Outright') {
        paygoFields.style.display = 'none';
        outrightFields.style.display = 'block';
    } else {
        paygoFields.style.display = 'none';
        outrightFields.style.display = 'none';
    }
});
