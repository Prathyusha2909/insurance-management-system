# API Documentation

## Customer APIs
- POST /api/customers/register
- GET /api/customers/{id}
- PUT /api/customers/{id}
- GET /api/customers/{id}/policies
- GET /api/customers/{id}/claims

## Policy APIs
- POST /api/policies
- GET /api/policies/{id}
- GET /api/policies
- PUT /api/policies/{id}/approve
- PUT /api/policies/{id}/reject
- PUT /api/policies/{id}/cancel
- GET /api/policies/active
- GET /api/policies/expiring-soon

## Premium APIs
- POST /api/premium/calculate

## Claim APIs
- POST /api/claims
- GET /api/claims/{id}
- GET /api/claims
- PUT /api/claims/{id}/under-review
- PUT /api/claims/{id}/approve
- PUT /api/claims/{id}/reject
- PUT /api/claims/{id}/settle
- GET /api/claims/status/{status}

## Report APIs
- GET /api/reports/active-policies
- GET /api/reports/pending-claims
- GET /api/reports/approved-claims
- GET /api/reports/rejected-claims
- GET /api/reports/monthly-premium
- GET /api/reports/claims-by-policy-type
- GET /api/reports/expiring-soon
- GET /api/reports/customers-multiple-policies
