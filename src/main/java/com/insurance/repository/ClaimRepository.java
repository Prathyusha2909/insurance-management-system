package com.insurance.repository;

import com.insurance.entity.Claim;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ClaimRepository extends JpaRepository<Claim, Long> {
    Long countByClaimStatus(String status);
    List<Claim> findByClaimStatus(String status);
    List<Claim> findByCustomerCustomerId(Long customerId);
}
