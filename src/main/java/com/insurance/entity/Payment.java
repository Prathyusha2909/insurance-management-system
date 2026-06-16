package com.insurance.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "payments")
public class Payment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long paymentId;
    @ManyToOne
    @JoinColumn(name = "policy_id")
    private Policy policy;
    @ManyToOne
    @JoinColumn(name = "customer_id")
    private Customer customer;
    private BigDecimal amount;
    private String paymentStatus;
    private LocalDateTime paymentDate = LocalDateTime.now();

    public Long getPaymentId() { return paymentId; }
    public void setPaymentId(Long paymentId) { this.paymentId = paymentId; }
    public Policy getPolicy() { return policy; }
    public void setPolicy(Policy policy) { this.policy = policy; }
    public Customer getCustomer() { return customer; }
    public void setCustomer(Customer customer) { this.customer = customer; }
    public BigDecimal getAmount() { return amount; }
    public void setAmount(BigDecimal amount) { this.amount = amount; }
    public String getPaymentStatus() { return paymentStatus; }
    public void setPaymentStatus(String paymentStatus) { this.paymentStatus = paymentStatus; }
    public java.time.LocalDateTime getPaymentDate() { return paymentDate; }
    public void setPaymentDate(java.time.LocalDateTime paymentDate) { this.paymentDate = paymentDate; }
}
