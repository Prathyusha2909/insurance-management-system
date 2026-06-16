package com.insurance.service;

import com.insurance.dto.ReportResponse;
import com.insurance.entity.Claim;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
import com.insurance.repository.ClaimRepository;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.PolicyRepository;
import org.springframework.stereotype.Service;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class ReportService {
    private final PolicyRepository policyRepository;
    private final ClaimRepository claimRepository;
    private final CustomerRepository customerRepository;

    public ReportService(PolicyRepository policyRepository, ClaimRepository claimRepository, CustomerRepository customerRepository) {
        this.policyRepository = policyRepository;
        this.claimRepository = claimRepository;
        this.customerRepository = customerRepository;
    }

    public List<ReportResponse> getActivePoliciesReport() {
        long total = policyRepository.countByStatus("ACTIVE");
        return List.of(new ReportResponse("Total Active Policies", String.valueOf(total)));
    }

    public List<ReportResponse> getPendingClaimsReport() {
        long total = claimRepository.countByClaimStatus("SUBMITTED");
        return List.of(new ReportResponse("Pending Claims", String.valueOf(total)));
    }

    public List<ReportResponse> getApprovedClaimsReport() {
        long total = claimRepository.countByClaimStatus("APPROVED");
        return List.of(new ReportResponse("Approved Claims", String.valueOf(total)));
    }

    public List<ReportResponse> getRejectedClaimsReport() {
        long total = claimRepository.countByClaimStatus("REJECTED");
        return List.of(new ReportResponse("Rejected Claims", String.valueOf(total)));
    }

    public List<ReportResponse> getMonthlyPremiumReport() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM");
        Map<String, BigDecimal> summary = new HashMap<>();
        List<Policy> activePolicies = policyRepository.findByStatus("ACTIVE");
        for (Policy policy : activePolicies) {
            String key = policy.getCreatedAt().format(formatter);
            summary.put(key, summary.getOrDefault(key, BigDecimal.ZERO).add(policy.getPremiumAmount()));
        }
        List<ReportResponse> report = new ArrayList<>();
        summary.forEach((k, v) -> report.add(new ReportResponse(k, v.toPlainString())));
        return report;
    }

    public List<ReportResponse> getClaimAmountByPolicyTypeReport() {
        Map<String, BigDecimal> totals = new HashMap<>();
        for (Claim claim : claimRepository.findAll()) {
            totals.merge(claim.getPolicy().getPolicyType(), claim.getClaimAmount(), BigDecimal::add);
        }
        List<ReportResponse> results = new ArrayList<>();
        totals.forEach((type, amount) -> results.add(new ReportResponse(type, amount.toPlainString())));
        return results;
    }

    public List<ReportResponse> getExpiringPoliciesReport() {
        LocalDate from = LocalDate.now();
        LocalDate to = from.plusDays(30);
        List<Policy> expiring = policyRepository.findByEndDateBetween(from, to);
        List<ReportResponse> results = new ArrayList<>();
        expiring.forEach(policy -> results.add(new ReportResponse(policy.getPolicyType(), policy.getEndDate().toString())));
        return results;
    }

    public List<ReportResponse> getCustomersWithMultiplePoliciesReport() {
        Map<Long, Integer> counter = new HashMap<>();
        for (Policy policy : policyRepository.findAll()) {
            Long customerId = policy.getCustomer().getCustomerId();
            counter.put(customerId, counter.getOrDefault(customerId, 0) + 1);
        }
        List<ReportResponse> results = new ArrayList<>();
        for (Map.Entry<Long, Integer> entry : counter.entrySet()) {
            if (entry.getValue() > 1) {
                Customer customer = customerRepository.findById(entry.getKey()).orElse(null);
                String label = customer == null ? "Customer #" + entry.getKey() : customer.getUser().getFullName();
                results.add(new ReportResponse(label, String.valueOf(entry.getValue())));
            }
        }
        return results;
    }
}
