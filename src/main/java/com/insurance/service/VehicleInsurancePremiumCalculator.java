package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("VEHICLE")
public class VehicleInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.04));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getVehicleAge() != null && request.getVehicleAge() > 5) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.15)));
        }
        if (Boolean.TRUE.equals(request.getAccidentHistory())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
