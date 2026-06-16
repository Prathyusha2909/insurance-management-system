package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("LIFE")
public class LifeInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.02));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getAge() != null && request.getAge() > 45) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        if (Boolean.TRUE.equals(request.getSmoker())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.25)));
        }
        if (request.getSumInsured().compareTo(BigDecimal.valueOf(1000000)) > 0) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.10)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
