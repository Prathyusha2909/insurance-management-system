package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;

public interface PremiumCalculator {
    PremiumResponse calculatePremium(PremiumRequest request);
}
