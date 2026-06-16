const premiumForm = document.getElementById('premiumForm');
premiumForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(premiumForm);
    const payload = {
        policyType: formData.get('policyType'),
        age: Number(formData.get('age')),
        sumInsured: Number(formData.get('sumInsured')),
        smoker: formData.get('smoker') === 'on',
        preExistingDisease: formData.get('preExistingDisease') === 'on',
        vehicleAge: Number(formData.get('vehicleAge')) || 0,
        accidentHistory: formData.get('accidentHistory') === 'on',
        propertyAge: Number(formData.get('propertyAge')) || 0,
        highRiskLocation: formData.get('highRiskLocation') === 'on'
    };
    const response = await fetch('/api/premium/calculate', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const result = document.getElementById('result');
    if (response.ok) {
        const data = await response.json();
        result.innerHTML = `<strong>Policy Type:</strong> ${data.policyType}<br><strong>Base Premium:</strong> ${data.basePremium}<br><strong>Risk Loading:</strong> ${data.riskLoading}<br><strong>Final Premium:</strong> ${data.finalPremium}`;
    } else {
        const body = await response.json();
        result.textContent = body.error || JSON.stringify(body);
    }
});
