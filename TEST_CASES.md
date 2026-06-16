# Test Cases

## PremiumCalculationServiceTest
- Life insurance premium for smoker above 45
- Health insurance premium with pre-existing disease
- Vehicle insurance premium with accident history
- Property insurance premium in high-risk location
- Invalid policy type should return error

## PolicyServiceTest
- Create valid policy request
- Reject policy with invalid dates
- Approve pending policy
- Cancel active policy
- Prevent policy creation with zero sum insured

## ClaimServiceTest
- Submit claim for active policy
- Reject claim for expired or inactive policy
- Approve claim under valid conditions
- Reject claim if claim amount exceeds sum insured
- Settle only approved claims
