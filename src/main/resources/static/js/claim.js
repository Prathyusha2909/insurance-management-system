const claimForm = document.getElementById('claimForm');
claimForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(claimForm);
    const payload = {
        policyId: Number(formData.get('policyId')),
        customerId: Number(formData.get('customerId')),
        claimAmount: Number(formData.get('claimAmount')),
        claimReason: formData.get('claimReason')
    };
    const response = await fetch('/api/claims', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const message = document.getElementById('claimMessage');
    if (response.ok) {
        message.textContent = 'Claim submitted successfully.';
    } else {
        const body = await response.json();
        message.textContent = body.error || JSON.stringify(body);
    }
});
