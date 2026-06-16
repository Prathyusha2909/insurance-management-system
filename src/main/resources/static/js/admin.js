const loadReports = document.getElementById('loadReports');
loadReports?.addEventListener('click', async () => {
    const sections = [
        {title: 'Active Policies', path: '/api/reports/active-policies'},
        {title: 'Pending Claims', path: '/api/reports/pending-claims'},
        {title: 'Approved Claims', path: '/api/reports/approved-claims'},
        {title: 'Rejected Claims', path: '/api/reports/rejected-claims'},
        {title: 'Monthly Premium', path: '/api/reports/monthly-premium'},
        {title: 'Claims by Policy Type', path: '/api/reports/claims-by-policy-type'},
        {title: 'Expiring Soon Policies', path: '/api/reports/expiring-soon'},
        {title: 'Customers with Multiple Policies', path: '/api/reports/customers-multiple-policies'}
    ];
    const container = document.getElementById('reports');
    container.innerHTML = '';
    for (const section of sections) {
        const response = await fetch(section.path);
        const data = await response.json();
        const sectionDiv = document.createElement('div');
        sectionDiv.innerHTML = `<h2>${section.title}</h2><pre>${JSON.stringify(data, null, 2)}</pre>`;
        container.appendChild(sectionDiv);
    }
});
