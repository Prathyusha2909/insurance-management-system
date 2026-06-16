package com.insurance.controller;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.PremiumCalculationService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/premium")
public class PremiumController {
    private final PremiumCalculationService premiumCalculationService;

    public PremiumController(PremiumCalculationService premiumCalculationService) {
        this.premiumCalculationService = premiumCalculationService;
    }

    @PostMapping("/calculate")
    public ResponseEntity<PremiumResponse> calculate(@Valid @RequestBody PremiumRequest request) {
        return ResponseEntity.ok(premiumCalculationService.calculatePremium(request));
    }
}
