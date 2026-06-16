package com.insurance.service;

import com.insurance.dto.PolicyRequest;
import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
import com.insurance.exception.InvalidRequestException;
import com.insurance.exception.ResourceNotFoundException;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.PolicyRepository;
import org.springframework.stereotype.Service;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeParseException;
import java.util.List;

@Service
public class PolicyService {
    private final PolicyRepository policyRepository;
    private final CustomerRepository customerRepository;
    private final PremiumCalculationService premiumCalculationService;

    public PolicyService(PolicyRepository policyRepository, CustomerRepository customerRepository, PremiumCalculationService premiumCalculationService) {
        this.policyRepository = policyRepository;
        this.customerRepository = customerRepository;
        this.premiumCalculationService = premiumCalculationService;
    }

    public Policy createPolicy(PolicyRequest request) {
        if (request.getSumInsured().compareTo(BigDecimal.ZERO) <= 0) {
            throw new InvalidRequestException("Sum insured must be greater than zero");
        }
        Customer customer = customerRepository.findById(request.getCustomerId())
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found"));
        LocalDate startDate;
        LocalDate endDate;
        try {
            startDate = LocalDate.parse(request.getStartDate());
            endDate = LocalDate.parse(request.getEndDate());
        } catch (DateTimeParseException ex) {
            throw new InvalidRequestException("Invalid date format. Expected yyyy-MM-dd");
        }
        if (!endDate.isAfter(startDate)) {
            throw new InvalidRequestException("Policy end date must be after start date");
        }

        Policy policy = new Policy();
        policy.setCustomer(customer);
        policy.setPolicyType(request.getPolicyType().toUpperCase());
        policy.setSumInsured(request.getSumInsured());
        policy.setStartDate(startDate);
        policy.setEndDate(endDate);
        policy.setStatus("PENDING");

        PremiumRequest premiumRequest = new PremiumRequest();
        premiumRequest.setPolicyType(request.getPolicyType().toUpperCase());
        premiumRequest.setAge(calculateCustomerAge(customer));
        premiumRequest.setSumInsured(request.getSumInsured());
        PremiumResponse premiumResponse = premiumCalculationService.calculatePremium(premiumRequest);
        policy.setPremiumAmount(premiumResponse.getFinalPremium());
        return policyRepository.save(policy);
    }

    private int calculateCustomerAge(Customer customer) {
        if (customer.getDateOfBirth() == null) {
            throw new InvalidRequestException("Customer date of birth is required for premium calculation");
        }
        return Period.between(customer.getDateOfBirth(), LocalDate.now()).getYears();
    }

    public Policy getPolicy(Long id) {
        return policyRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Policy not found"));
    }

    public List<Policy> getAllPolicies() {
        return policyRepository.findAll();
    }

    public List<Policy> getPoliciesByCustomer(Long customerId) {
        return policyRepository.findByCustomerCustomerId(customerId);
    }

    public Policy approvePolicy(Long id) {
        Policy policy = getPolicy(id);
        if (!"PENDING".equals(policy.getStatus())) {
            throw new InvalidRequestException("Only pending policies can be approved");
        }
        policy.setStatus("ACTIVE");
        return policyRepository.save(policy);
    }

    public Policy rejectPolicy(Long id) {
        Policy policy = getPolicy(id);
        if (!"PENDING".equals(policy.getStatus())) {
            throw new InvalidRequestException("Only pending policies can be rejected");
        }
        policy.setStatus("REJECTED");
        return policyRepository.save(policy);
    }

    public Policy cancelPolicy(Long id) {
        Policy policy = getPolicy(id);
        if ("CANCELLED".equals(policy.getStatus()) || "EXPIRED".equals(policy.getStatus())) {
            throw new InvalidRequestException("Policy is already inactive");
        }
        policy.setStatus("CANCELLED");
        return policyRepository.save(policy);
    }

    public List<Policy> getActivePolicies() {
        return policyRepository.findByStatus("ACTIVE");
    }

    public List<Policy> getExpiringSoonPolicies() {
        LocalDate today = LocalDate.now();
        return policyRepository.findByEndDateBetween(today, today.plusDays(30));
    }
}
