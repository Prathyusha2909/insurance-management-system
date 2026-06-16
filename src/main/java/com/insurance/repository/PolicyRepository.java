package com.insurance.repository;

import com.insurance.entity.Policy;
import org.springframework.data.jpa.repository.JpaRepository;
import java.time.LocalDate;
import java.util.List;

public interface PolicyRepository extends JpaRepository<Policy, Long> {
    Long countByStatus(String status);
    List<Policy> findByStatus(String status);
    List<Policy> findByEndDateBetween(LocalDate start, LocalDate end);
    List<Policy> findByCustomerCustomerId(Long customerId);
}
