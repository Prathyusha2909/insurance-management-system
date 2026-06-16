const registrationForm = document.getElementById('registrationForm');
registrationForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(registrationForm);
    const payload = Object.fromEntries(formData.entries());
    const response = await fetch('/api/customers/register', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const message = document.getElementById('message');
    if (response.ok) {
        message.textContent = 'Registration successful. Customer created.';
    } else {
        const body = await response.json();
        message.textContent = body.error || JSON.stringify(body);
    }
});
