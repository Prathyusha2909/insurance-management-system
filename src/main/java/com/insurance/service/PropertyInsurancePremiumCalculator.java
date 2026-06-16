package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("PROPERTY")
public class PropertyInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.015));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getPropertyAge() != null && request.getPropertyAge() > 10) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.10)));
        }
        if (Boolean.TRUE.equals(request.getHighRiskLocation())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
