package com.insurance.controller;

import com.insurance.dto.PolicyRequest;
import com.insurance.entity.Policy;
import com.insurance.service.PolicyService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/policies")
public class PolicyController {
    private final PolicyService policyService;

    public PolicyController(PolicyService policyService) {
        this.policyService = policyService;
    }

    @PostMapping
    public ResponseEntity<Policy> createPolicy(@Valid @RequestBody PolicyRequest request) {
        return ResponseEntity.ok(policyService.createPolicy(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Policy> getPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.getPolicy(id));
    }

    @GetMapping
    public ResponseEntity<List<Policy>> getAllPolicies() {
        return ResponseEntity.ok(policyService.getAllPolicies());
    }

    @PutMapping("/{id}/approve")
    public ResponseEntity<Policy> approvePolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.approvePolicy(id));
    }

    @PutMapping("/{id}/reject")
    public ResponseEntity<Policy> rejectPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.rejectPolicy(id));
    }

    @PutMapping("/{id}/cancel")
    public ResponseEntity<Policy> cancelPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.cancelPolicy(id));
    }

    @GetMapping("/active")
    public ResponseEntity<List<Policy>> getActivePolicies() {
        return ResponseEntity.ok(policyService.getActivePolicies());
    }

    @GetMapping("/expiring-soon")
    public ResponseEntity<List<Policy>> getExpiringSoonPolicies() {
        return ResponseEntity.ok(policyService.getExpiringSoonPolicies());
    }
}
