package com.insurance;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.HealthInsurancePremiumCalculator;
import com.insurance.service.LifeInsurancePremiumCalculator;
import com.insurance.service.PremiumCalculationService;
import com.insurance.service.PropertyInsurancePremiumCalculator;
import com.insurance.service.VehicleInsurancePremiumCalculator;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class PremiumCalculationServiceTest {
    private PremiumCalculationService service;

    @BeforeEach
    public void setup() {
        Map<String, Object> calculators = new HashMap<>();
        calculators.put("LIFE", new LifeInsurancePremiumCalculator());
        calculators.put("HEALTH", new HealthInsurancePremiumCalculator());
        calculators.put("VEHICLE", new VehicleInsurancePremiumCalculator());
        calculators.put("PROPERTY", new PropertyInsurancePremiumCalculator());
        service = new PremiumCalculationService((Map) calculators);
    }

    @Test
    public void testLifeInsurancePremiumForSmokerAbove45() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("LIFE");
        request.setAge(48);
        request.setSumInsured(BigDecimal.valueOf(1000000));
        request.setSmoker(true);

        PremiumResponse response = service.calculatePremium(request);

        assertNotNull(response);
        assertEquals("LIFE", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }

    @Test
    public void testHealthInsurancePremiumWithPreExistingDisease() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("HEALTH");
        request.setAge(55);
        request.setSumInsured(BigDecimal.valueOf(500000));
        request.setPreExistingDisease(true);

        PremiumResponse response = service.calculatePremium(request);

        assertEquals("HEALTH", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }

    @Test
    public void testVehicleInsurancePremiumForAccidentHistory() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("VEHICLE");
        request.setAge(40);
        request.setSumInsured(BigDecimal.valueOf(300000));
        request.setAccidentHistory(true);

        PremiumResponse response = service.calculatePremium(request);

        assertEquals("VEHICLE", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }

    @Test
    public void testPropertyInsurancePremiumForHighRiskLocation() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("PROPERTY");
        request.setAge(50);
        request.setSumInsured(BigDecimal.valueOf(800000));
        request.setHighRiskLocation(true);

        PremiumResponse response = service.calculatePremium(request);

        assertEquals("PROPERTY", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }

    @Test
    public void testUnsupportedPolicyTypeThrowsException() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("TRAVEL");
        request.setAge(35);
        request.setSumInsured(BigDecimal.valueOf(200000));

        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> service.calculatePremium(request));
        assertTrue(exception.getMessage().contains("Unsupported policy type"));
    }
}
