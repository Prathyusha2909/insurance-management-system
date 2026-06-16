package com.insurance.controller;

import com.insurance.dto.CustomerRequest;
import com.insurance.entity.Customer;
import com.insurance.service.CustomerService;
import com.insurance.service.PolicyService;
import com.insurance.service.ClaimService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/customers")
public class CustomerController {
    private final CustomerService customerService;
    private final PolicyService policyService;
    private final ClaimService claimService;

    public CustomerController(CustomerService customerService, PolicyService policyService, ClaimService claimService) {
        this.customerService = customerService;
        this.policyService = policyService;
        this.claimService = claimService;
    }

    @PostMapping("/register")
    public ResponseEntity<Customer> registerCustomer(@Valid @RequestBody CustomerRequest request) {
        return ResponseEntity.ok(customerService.registerCustomer(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Customer> getCustomer(@PathVariable Long id) {
        return ResponseEntity.ok(customerService.getCustomer(id));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Customer> updateCustomer(@PathVariable Long id, @Valid @RequestBody CustomerRequest request) {
        return ResponseEntity.ok(customerService.updateCustomer(id, request));
    }

    @GetMapping("/{id}/policies")
    public ResponseEntity<List<?>> getCustomerPolicies(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.getPoliciesByCustomer(id));
    }

    @GetMapping("/{id}/claims")
    public ResponseEntity<List<?>> getCustomerClaims(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.getClaimsByCustomer(id));
    }
}
