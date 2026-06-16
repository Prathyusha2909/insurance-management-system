package com.insurance.service;

import com.insurance.dto.ClaimRequest;
import com.insurance.entity.Claim;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
import com.insurance.exception.InvalidRequestException;
import com.insurance.exception.ResourceNotFoundException;
import com.insurance.repository.ClaimRepository;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.PolicyRepository;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class ClaimService {
    private final ClaimRepository claimRepository;
    private final PolicyRepository policyRepository;
    private final CustomerRepository customerRepository;

    public ClaimService(ClaimRepository claimRepository, PolicyRepository policyRepository, CustomerRepository customerRepository) {
        this.claimRepository = claimRepository;
        this.policyRepository = policyRepository;
        this.customerRepository = customerRepository;
    }

    public Claim submitClaim(ClaimRequest request) {
        Policy policy = policyRepository.findById(request.getPolicyId())
                .orElseThrow(() -> new ResourceNotFoundException("Policy not found"));
        Customer customer = customerRepository.findById(request.getCustomerId())
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found"));
        if (!"ACTIVE".equals(policy.getStatus())) {
            throw new InvalidRequestException("Claims can only be submitted for active policies");
        }
        if (request.getClaimAmount().compareTo(policy.getSumInsured()) > 0) {
            throw new InvalidRequestException("Claim amount cannot exceed sum insured");
        }
        Claim claim = new Claim();
        claim.setPolicy(policy);
        claim.setCustomer(customer);
        claim.setClaimAmount(request.getClaimAmount());
        claim.setClaimReason(request.getClaimReason());
        claim.setClaimStatus("SUBMITTED");
        claim.setCreatedAt(LocalDateTime.now());
        claim.setUpdatedAt(LocalDateTime.now());
        return claimRepository.save(claim);
    }

    public Claim getClaim(Long id) {
        return claimRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Claim not found"));
    }

    public List<Claim> getAllClaims() {
        return claimRepository.findAll();
    }

    public Claim reviewClaim(Long id) {
        Claim claim = getClaim(id);
        if (!"SUBMITTED".equals(claim.getClaimStatus())) {
            throw new InvalidRequestException("Only submitted claims can move to under review");
        }
        claim.setClaimStatus("UNDER_REVIEW");
        claim.setUpdatedAt(LocalDateTime.now());
        return claimRepository.save(claim);
    }

    public Claim approveClaim(Long id) {
        Claim claim = getClaim(id);
        if (!"SUBMITTED".equals(claim.getClaimStatus()) && !"UNDER_REVIEW".equals(claim.getClaimStatus())) {
            throw new InvalidRequestException("Only claims under review or submitted can be approved");
        }
        claim.setClaimStatus("APPROVED");
        claim.setUpdatedAt(LocalDateTime.now());
        return claimRepository.save(claim);
    }

    public Claim rejectClaim(Long id) {
        Claim claim = getClaim(id);
        if (!"SUBMITTED".equals(claim.getClaimStatus()) && !"UNDER_REVIEW".equals(claim.getClaimStatus())) {
            throw new InvalidRequestException("Only submitted or under review claims can be rejected");
        }
        claim.setClaimStatus("REJECTED");
        claim.setUpdatedAt(LocalDateTime.now());
        return claimRepository.save(claim);
    }

    public Claim settleClaim(Long id) {
        Claim claim = getClaim(id);
        if (!"APPROVED".equals(claim.getClaimStatus())) {
            throw new InvalidRequestException("Only approved claims can be settled");
        }
        claim.setClaimStatus("SETTLED");
        claim.setUpdatedAt(LocalDateTime.now());
        return claimRepository.save(claim);
    }

    public List<Claim> getClaimsByStatus(String status) {
        return claimRepository.findByClaimStatus(status);
    }

    public List<Claim> getClaimsByCustomer(Long customerId) {
        return claimRepository.findByCustomerCustomerId(customerId);
    }
}
