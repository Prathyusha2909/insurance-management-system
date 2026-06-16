package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.exception.InvalidRequestException;
import org.springframework.stereotype.Service;
import java.util.Map;

@Service
public class PremiumCalculationService {
    private final Map<String, PremiumCalculator> calculators;

    public PremiumCalculationService(Map<String, PremiumCalculator> calculators) {
        this.calculators = calculators;
    }

    public PremiumResponse calculatePremium(PremiumRequest request) {
        if (request.getPolicyType() == null || request.getPolicyType().isBlank()) {
            throw new InvalidRequestException("Policy type is required");
        }
        PremiumCalculator calculator = calculators.get(request.getPolicyType().toUpperCase());
        if (calculator == null) {
            throw new InvalidRequestException("Unsupported policy type: " + request.getPolicyType());
        }
        return calculator.calculatePremium(request);
    }
}
