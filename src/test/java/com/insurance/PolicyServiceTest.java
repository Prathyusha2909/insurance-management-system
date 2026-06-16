package com.insurance;

import com.insurance.dto.PolicyRequest;
import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
import com.insurance.entity.User;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.PolicyRepository;
import com.insurance.service.PolicyService;
import com.insurance.service.PremiumCalculationService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import java.math.BigDecimal;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;

public class PolicyServiceTest {
    private PolicyService policyService;
    private PolicyRepository policyRepository;
    private CustomerRepository customerRepository;
    private PremiumCalculationService premiumCalculationService;

    @BeforeEach
    public void setup() {
        policyRepository = Mockito.mock(PolicyRepository.class);
        customerRepository = Mockito.mock(CustomerRepository.class);
        premiumCalculationService = Mockito.mock(PremiumCalculationService.class);
        policyService = new PolicyService(policyRepository, customerRepository, premiumCalculationService);
    }

    @Test
    public void testCreatePolicy() {
        User user = new User(); user.setUserId(1L);
        user.setFullName("Jane Doe");
        Customer customer = new Customer(); customer.setCustomerId(1L); customer.setUser(user);
        PolicyRequest request = new PolicyRequest();
        request.setCustomerId(1L);
        request.setPolicyType("LIFE");
        request.setSumInsured(BigDecimal.valueOf(100000));
        request.setStartDate("2025-01-01");
        request.setEndDate("2026-01-01");
        Mockito.when(customerRepository.findById(1L)).thenReturn(Optional.of(customer));
        Mockito.when(premiumCalculationService.calculatePremium(any(PremiumRequest.class)))
                .thenReturn(new PremiumResponse("LIFE", BigDecimal.valueOf(2000), BigDecimal.valueOf(0), BigDecimal.valueOf(2000)));
        Mockito.when(policyRepository.save(any(Policy.class))).thenAnswer(invocation -> invocation.getArgument(0));
        Policy policy = policyService.createPolicy(request);
        assertEquals("PENDING", policy.getStatus());
        assertNotNull(policy.getPremiumAmount());
    }
}
