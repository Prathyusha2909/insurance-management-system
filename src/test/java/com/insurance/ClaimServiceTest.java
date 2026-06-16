package com.insurance;

import com.insurance.dto.ClaimRequest;
import com.insurance.entity.Claim;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
import com.insurance.exception.InvalidRequestException;
import com.insurance.repository.ClaimRepository;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.PolicyRepository;
import com.insurance.service.ClaimService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.math.BigDecimal;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;

public class ClaimServiceTest {
    private ClaimService claimService;
    private ClaimRepository claimRepository;
    private PolicyRepository policyRepository;
    private CustomerRepository customerRepository;

    @BeforeEach
    public void setup() {
        claimRepository = Mockito.mock(ClaimRepository.class);
        policyRepository = Mockito.mock(PolicyRepository.class);
        customerRepository = Mockito.mock(CustomerRepository.class);
        claimService = new ClaimService(claimRepository, policyRepository, customerRepository);
    }

    @Test
    public void testSubmitClaimForActivePolicy() {
        Policy policy = new Policy();
        policy.setPolicyId(1L);
        policy.setStatus("ACTIVE");
        policy.setSumInsured(BigDecimal.valueOf(10000));

        Customer customer = new Customer();
        customer.setCustomerId(1L);

        ClaimRequest request = new ClaimRequest();
        request.setPolicyId(1L);
        request.setCustomerId(1L);
        request.setClaimAmount(BigDecimal.valueOf(5000));
        request.setClaimReason("Accident damage");

        Mockito.when(policyRepository.findById(1L)).thenReturn(Optional.of(policy));
        Mockito.when(customerRepository.findById(1L)).thenReturn(Optional.of(customer));
        Mockito.when(claimRepository.save(any(Claim.class))).thenAnswer(invocation -> invocation.getArgument(0));

        Claim claim = claimService.submitClaim(request);

        assertEquals("SUBMITTED", claim.getClaimStatus());
        assertEquals(BigDecimal.valueOf(5000), claim.getClaimAmount());
    }

    @Test
    public void testSubmitClaimForInactivePolicyThrows() {
        Policy policy = new Policy();
        policy.setPolicyId(1L);
        policy.setStatus("REJECTED");
        policy.setSumInsured(BigDecimal.valueOf(10000));

        Customer customer = new Customer();
        customer.setCustomerId(1L);

        ClaimRequest request = new ClaimRequest();
        request.setPolicyId(1L);
        request.setCustomerId(1L);
        request.setClaimAmount(BigDecimal.valueOf(1000));
        request.setClaimReason("Damage");

        Mockito.when(policyRepository.findById(1L)).thenReturn(Optional.of(policy));
        Mockito.when(customerRepository.findById(1L)).thenReturn(Optional.of(customer));

        assertThrows(InvalidRequestException.class, () -> claimService.submitClaim(request));
    }

    @Test
    public void testSubmitClaimAboveSumInsuredThrows() {
        Policy policy = new Policy();
        policy.setPolicyId(1L);
        policy.setStatus("ACTIVE");
        policy.setSumInsured(BigDecimal.valueOf(5000));

        Customer customer = new Customer();
        customer.setCustomerId(1L);

        ClaimRequest request = new ClaimRequest();
        request.setPolicyId(1L);
        request.setCustomerId(1L);
        request.setClaimAmount(BigDecimal.valueOf(6000));
        request.setClaimReason("Accident");

        Mockito.when(policyRepository.findById(1L)).thenReturn(Optional.of(policy));
        Mockito.when(customerRepository.findById(1L)).thenReturn(Optional.of(customer));

        assertThrows(InvalidRequestException.class, () -> claimService.submitClaim(request));
    }

    @Test
    public void testApproveSubmittedClaim() {
        Claim claim = new Claim();
        claim.setClaimId(1L);
        claim.setClaimStatus("SUBMITTED");

        Mockito.when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));
        Mockito.when(claimRepository.save(any(Claim.class))).thenAnswer(invocation -> invocation.getArgument(0));

        Claim approved = claimService.approveClaim(1L);

        assertEquals("APPROVED", approved.getClaimStatus());
    }

    @Test
    public void testSettleApprovedClaim() {
        Claim claim = new Claim();
        claim.setClaimId(1L);
        claim.setClaimStatus("APPROVED");

        Mockito.when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));
        Mockito.when(claimRepository.save(any(Claim.class))).thenAnswer(invocation -> invocation.getArgument(0));

        Claim settled = claimService.settleClaim(1L);

        assertEquals("SETTLED", settled.getClaimStatus());
    }
}
