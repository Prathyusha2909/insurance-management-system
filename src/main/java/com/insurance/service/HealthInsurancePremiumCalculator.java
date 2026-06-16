package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("HEALTH")
public class HealthInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.03));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getAge() != null && request.getAge() > 50) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.30)));
        }
        if (Boolean.TRUE.equals(request.getPreExistingDisease())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.25)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
