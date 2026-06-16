package com.insurance.controller;

import com.insurance.dto.ClaimRequest;
import com.insurance.entity.Claim;
import com.insurance.service.ClaimService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/claims")
public class ClaimController {
    private final ClaimService claimService;

    public ClaimController(ClaimService claimService) {
        this.claimService = claimService;
    }

    @PostMapping
    public ResponseEntity<Claim> submitClaim(@Valid @RequestBody ClaimRequest request) {
        return ResponseEntity.ok(claimService.submitClaim(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Claim> getClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.getClaim(id));
    }

    @GetMapping
    public ResponseEntity<List<Claim>> getAllClaims() {
        return ResponseEntity.ok(claimService.getAllClaims());
    }

    @PutMapping("/{id}/under-review")
    public ResponseEntity<Claim> reviewClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.reviewClaim(id));
    }

    @PutMapping("/{id}/approve")
    public ResponseEntity<Claim> approveClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.approveClaim(id));
    }

    @PutMapping("/{id}/reject")
    public ResponseEntity<Claim> rejectClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.rejectClaim(id));
    }

    @PutMapping("/{id}/settle")
    public ResponseEntity<Claim> settleClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.settleClaim(id));
    }

    @GetMapping("/status/{status}")
    public ResponseEntity<List<Claim>> getClaimsByStatus(@PathVariable String status) {
        return ResponseEntity.ok(claimService.getClaimsByStatus(status.toUpperCase()));
    }
}
