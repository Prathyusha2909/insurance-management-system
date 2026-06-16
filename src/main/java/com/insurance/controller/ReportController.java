package com.insurance.controller;

import com.insurance.dto.ReportResponse;
import com.insurance.service.ReportService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/reports")
public class ReportController {
    private final ReportService reportService;

    public ReportController(ReportService reportService) {
        this.reportService = reportService;
    }

    @GetMapping("/active-policies")
    public ResponseEntity<List<ReportResponse>> activePolicies() {
        return ResponseEntity.ok(reportService.getActivePoliciesReport());
    }

    @GetMapping("/pending-claims")
    public ResponseEntity<List<ReportResponse>> pendingClaims() {
        return ResponseEntity.ok(reportService.getPendingClaimsReport());
    }

    @GetMapping("/approved-claims")
    public ResponseEntity<List<ReportResponse>> approvedClaims() {
        return ResponseEntity.ok(reportService.getApprovedClaimsReport());
    }

    @GetMapping("/rejected-claims")
    public ResponseEntity<List<ReportResponse>> rejectedClaims() {
        return ResponseEntity.ok(reportService.getRejectedClaimsReport());
    }

    @GetMapping("/monthly-premium")
    public ResponseEntity<List<ReportResponse>> monthlyPremium() {
        return ResponseEntity.ok(reportService.getMonthlyPremiumReport());
    }

    @GetMapping("/claims-by-policy-type")
    public ResponseEntity<List<ReportResponse>> claimsByPolicyType() {
        return ResponseEntity.ok(reportService.getClaimAmountByPolicyTypeReport());
    }

    @GetMapping("/expiring-soon")
    public ResponseEntity<List<ReportResponse>> expiringSoon() {
        return ResponseEntity.ok(reportService.getExpiringPoliciesReport());
    }

    @GetMapping("/customers-multiple-policies")
    public ResponseEntity<List<ReportResponse>> customersWithMultiplePolicies() {
        return ResponseEntity.ok(reportService.getCustomersWithMultiplePoliciesReport());
    }
}
