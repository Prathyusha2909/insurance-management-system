package com.insurance.soap;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.PremiumCalculationService;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

@Endpoint
public class PremiumEndpoint {
    private static final String NAMESPACE_URI = "http://insurance.com/soap";
    private final PremiumCalculationService premiumCalculationService;

    public PremiumEndpoint(PremiumCalculationService premiumCalculationService) {
        this.premiumCalculationService = premiumCalculationService;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "calculatePremiumRequest")
    @ResponsePayload
    public CalculatePremiumResponse calculatePremium(@RequestPayload CalculatePremiumRequest request) {
        PremiumRequest premiumRequest = new PremiumRequest();
        premiumRequest.setPolicyType(request.getPolicyType());
        premiumRequest.setAge(request.getAge());
        premiumRequest.setSumInsured(request.getSumInsured());
        premiumRequest.setSmoker(request.isSmoker());
        premiumRequest.setPreExistingDisease(request.isPreExistingDisease());
        premiumRequest.setVehicleAge(request.getVehicleAge());
        premiumRequest.setAccidentHistory(request.isAccidentHistory());
        premiumRequest.setPropertyAge(request.getPropertyAge());
        premiumRequest.setHighRiskLocation(request.isHighRiskLocation());

        PremiumResponse response = premiumCalculationService.calculatePremium(premiumRequest);
        CalculatePremiumResponse soapResponse = new CalculatePremiumResponse();
        soapResponse.setPolicyType(response.getPolicyType());
        soapResponse.setBasePremium(response.getBasePremium());
        soapResponse.setRiskLoading(response.getRiskLoading());
        soapResponse.setFinalPremium(response.getFinalPremium());
        return soapResponse;
    }
}
