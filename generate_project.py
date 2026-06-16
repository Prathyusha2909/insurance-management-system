from pathlib import Path
root = Path(r'c:\Users\prath\Desktop\Insurance policy')
files = {
    'pom.xml': '''<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.insurance</groupId>
    <artifactId>insurance-management-system</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>
    <name>Insurance Management System</name>
    <description>Insurance Policy & Claims Management System</description>
    <properties>
        <java.version>17</java.version>
        <spring.boot.version>3.2.0</spring.boot.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring.boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web-services</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.1.0</version>
        </dependency>
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>jakarta.xml.bind</groupId>
            <artifactId>jakarta.xml.bind-api</artifactId>
        </dependency>
        <dependency>
            <groupId>org.glassfish.jaxb</groupId>
            <artifactId>jaxb-runtime</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
''',
    'src/main/resources/application.properties': '''spring.datasource.url=jdbc:h2:mem:insurance;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.h2.console.enabled=true
springdoc.api-docs.path=/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
server.port=8080
''',
    'src/main/resources/premium.xsd': '''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://insurance.com/soap" xmlns:tns="http://insurance.com/soap" elementFormDefault="qualified">
    <xs:element name="calculatePremiumRequest">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="policyType" type="xs:string"/>
                <xs:element name="age" type="xs:int"/>
                <xs:element name="sumInsured" type="xs:decimal"/>
                <xs:element name="smoker" type="xs:boolean"/>
                <xs:element name="preExistingDisease" type="xs:boolean"/>
                <xs:element name="vehicleAge" type="xs:int"/>
                <xs:element name="accidentHistory" type="xs:boolean"/>
                <xs:element name="propertyAge" type="xs:int"/>
                <xs:element name="highRiskLocation" type="xs:boolean"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="calculatePremiumResponse">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="policyType" type="xs:string"/>
                <xs:element name="basePremium" type="xs:decimal"/>
                <xs:element name="riskLoading" type="xs:decimal"/>
                <xs:element name="finalPremium" type="xs:decimal"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
''',
    'src/main/java/com/insurance/InsuranceApplication.java': '''package com.insurance;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class InsuranceApplication {
    public static void main(String[] args) {
        SpringApplication.run(InsuranceApplication.class, args);
    }
}
''',
    'src/main/java/com/insurance/entity/User.java': '''package com.insurance.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;
    private String fullName;
    @Column(unique = true, nullable = false)
    private String email;
    @Column(nullable = false)
    private String password;
    private String role;
    private LocalDateTime createdAt = LocalDateTime.now();

    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
''',
    'src/main/java/com/insurance/entity/Customer.java': '''package com.insurance.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "customers")
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long customerId;
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "user_id")
    private User user;
    private String phone;
    private LocalDate dateOfBirth;
    private String gender;
    private String address;
    private LocalDateTime createdAt = LocalDateTime.now();

    public Long getCustomerId() { return customerId; }
    public void setCustomerId(Long customerId) { this.customerId = customerId; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public LocalDate getDateOfBirth() { return dateOfBirth; }
    public void setDateOfBirth(LocalDate dateOfBirth) { this.dateOfBirth = dateOfBirth; }
    public String getGender() { return gender; }
    public void setGender(String gender) { this.gender = gender; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
''',
    'src/main/java/com/insurance/entity/Policy.java': '''package com.insurance.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "policies")
public class Policy {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long policyId;
    @ManyToOne
    @JoinColumn(name = "customer_id")
    private Customer customer;
    private String policyType;
    private BigDecimal sumInsured;
    private BigDecimal premiumAmount;
    private LocalDate startDate;
    private LocalDate endDate;
    private String status;
    private LocalDateTime createdAt = LocalDateTime.now();

    public Long getPolicyId() { return policyId; }
    public void setPolicyId(Long policyId) { this.policyId = policyId; }
    public Customer getCustomer() { return customer; }
    public void setCustomer(Customer customer) { this.customer = customer; }
    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public BigDecimal getSumInsured() { return sumInsured; }
    public void setSumInsured(BigDecimal sumInsured) { this.sumInsured = sumInsured; }
    public BigDecimal getPremiumAmount() { return premiumAmount; }
    public void setPremiumAmount(BigDecimal premiumAmount) { this.premiumAmount = premiumAmount; }
    public LocalDate getStartDate() { return startDate; }
    public void setStartDate(LocalDate startDate) { this.startDate = startDate; }
    public LocalDate getEndDate() { return endDate; }
    public void setEndDate(LocalDate endDate) { this.endDate = endDate; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
''',
    'src/main/java/com/insurance/entity/Claim.java': '''package com.insurance.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "claims")
public class Claim {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long claimId;
    @ManyToOne
    @JoinColumn(name = "policy_id")
    private Policy policy;
    @ManyToOne
    @JoinColumn(name = "customer_id")
    private Customer customer;
    private BigDecimal claimAmount;
    private String claimReason;
    private String claimStatus;
    private String adminRemarks;
    private LocalDateTime createdAt = LocalDateTime.now();
    private LocalDateTime updatedAt = LocalDateTime.now();

    public Long getClaimId() { return claimId; }
    public void setClaimId(Long claimId) { this.claimId = claimId; }
    public Policy getPolicy() { return policy; }
    public void setPolicy(Policy policy) { this.policy = policy; }
    public Customer getCustomer() { return customer; }
    public void setCustomer(Customer customer) { this.customer = customer; }
    public BigDecimal getClaimAmount() { return claimAmount; }
    public void setClaimAmount(BigDecimal claimAmount) { this.claimAmount = claimAmount; }
    public String getClaimReason() { return claimReason; }
    public void setClaimReason(String claimReason) { this.claimReason = claimReason; }
    public String getClaimStatus() { return claimStatus; }
    public void setClaimStatus(String claimStatus) { this.claimStatus = claimStatus; }
    public String getAdminRemarks() { return adminRemarks; }
    public void setAdminRemarks(String adminRemarks) { this.adminRemarks = adminRemarks; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}
''',
    'src/main/java/com/insurance/entity/Payment.java': '''package com.insurance.entity;

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
''',
    'src/main/java/com/insurance/repository/UserRepository.java': '''package com.insurance.repository;

import com.insurance.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    boolean existsByEmail(String email);
}
''',
    'src/main/java/com/insurance/repository/CustomerRepository.java': '''package com.insurance.repository;

import com.insurance.entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface CustomerRepository extends JpaRepository<Customer, Long> {
    Optional<Customer> findByUserUserId(Long userId);
}
''',
    'src/main/java/com/insurance/repository/PolicyRepository.java': '''package com.insurance.repository;

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
''',
    'src/main/java/com/insurance/repository/ClaimRepository.java': '''package com.insurance.repository;

import com.insurance.entity.Claim;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ClaimRepository extends JpaRepository<Claim, Long> {
    Long countByClaimStatus(String status);
    List<Claim> findByClaimStatus(String status);
    List<Claim> findByCustomerCustomerId(Long customerId);
}
''',
    'src/main/java/com/insurance/repository/PaymentRepository.java': '''package com.insurance.repository;

import com.insurance.entity.Payment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PaymentRepository extends JpaRepository<Payment, Long> {
}
''',
    'src/main/java/com/insurance/dto/CustomerRequest.java': '''package com.insurance.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public class CustomerRequest {
    @NotBlank
    private String fullName;
    @Email
    @NotBlank
    private String email;
    @NotBlank
    private String password;
    @NotBlank
    private String role;
    @NotBlank
    private String phone;
    @NotBlank
    private String dateOfBirth;
    @NotBlank
    private String gender;
    @NotBlank
    private String address;

    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getDateOfBirth() { return dateOfBirth; }
    public void setDateOfBirth(String dateOfBirth) { this.dateOfBirth = dateOfBirth; }
    public String getGender() { return gender; }
    public void setGender(String gender) { this.gender = gender; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
}
''',
    'src/main/java/com/insurance/dto/PolicyRequest.java': '''package com.insurance.dto;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

public class PolicyRequest {
    @NotNull
    private Long customerId;
    @NotBlank
    private String policyType;
    @NotNull
    @DecimalMin(value = "0.01", message = "Sum insured must be positive")
    private BigDecimal sumInsured;
    @NotNull
    private String startDate;
    @NotNull
    private String endDate;

    public Long getCustomerId() { return customerId; }
    public void setCustomerId(Long customerId) { this.customerId = customerId; }
    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public BigDecimal getSumInsured() { return sumInsured; }
    public void setSumInsured(BigDecimal sumInsured) { this.sumInsured = sumInsured; }
    public String getStartDate() { return startDate; }
    public void setStartDate(String startDate) { this.startDate = startDate; }
    public String getEndDate() { return endDate; }
    public void setEndDate(String endDate) { this.endDate = endDate; }
}
''',
    'src/main/java/com/insurance/dto/ClaimRequest.java': '''package com.insurance.dto;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

public class ClaimRequest {
    @NotNull
    private Long policyId;
    @NotNull
    private Long customerId;
    @DecimalMin(value = "0.01", message = "Claim amount must be positive")
    private BigDecimal claimAmount;
    @NotBlank
    private String claimReason;

    public Long getPolicyId() { return policyId; }
    public void setPolicyId(Long policyId) { this.policyId = policyId; }
    public Long getCustomerId() { return customerId; }
    public void setCustomerId(Long customerId) { this.customerId = customerId; }
    public BigDecimal getClaimAmount() { return claimAmount; }
    public void setClaimAmount(BigDecimal claimAmount) { this.claimAmount = claimAmount; }
    public String getClaimReason() { return claimReason; }
    public void setClaimReason(String claimReason) { this.claimReason = claimReason; }
}
''',
    'src/main/java/com/insurance/dto/PremiumRequest.java': '''package com.insurance.dto;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

public class PremiumRequest {
    @NotBlank
    private String policyType;
    @NotNull
    private Integer age;
    @NotNull
    @DecimalMin(value = "0.0", inclusive = false)
    private BigDecimal sumInsured;
    private Boolean smoker = false;
    private Boolean preExistingDisease = false;
    private Integer vehicleAge = 0;
    private Boolean accidentHistory = false;
    private Integer propertyAge = 0;
    private Boolean highRiskLocation = false;

    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
    public BigDecimal getSumInsured() { return sumInsured; }
    public void setSumInsured(BigDecimal sumInsured) { this.sumInsured = sumInsured; }
    public Boolean getSmoker() { return smoker; }
    public void setSmoker(Boolean smoker) { this.smoker = smoker; }
    public Boolean getPreExistingDisease() { return preExistingDisease; }
    public void setPreExistingDisease(Boolean preExistingDisease) { this.preExistingDisease = preExistingDisease; }
    public Integer getVehicleAge() { return vehicleAge; }
    public void setVehicleAge(Integer vehicleAge) { this.vehicleAge = vehicleAge; }
    public Boolean getAccidentHistory() { return accidentHistory; }
    public void setAccidentHistory(Boolean accidentHistory) { this.accidentHistory = accidentHistory; }
    public Integer getPropertyAge() { return propertyAge; }
    public void setPropertyAge(Integer propertyAge) { this.propertyAge = propertyAge; }
    public Boolean getHighRiskLocation() { return highRiskLocation; }
    public void setHighRiskLocation(Boolean highRiskLocation) { this.highRiskLocation = highRiskLocation; }
}
''',
    'src/main/java/com/insurance/dto/PremiumResponse.java': '''package com.insurance.dto;

import java.math.BigDecimal;

public class PremiumResponse {
    private String policyType;
    private BigDecimal basePremium;
    private BigDecimal riskLoading;
    private BigDecimal finalPremium;

    public PremiumResponse() {}
    public PremiumResponse(String policyType, BigDecimal basePremium, BigDecimal riskLoading, BigDecimal finalPremium) {
        this.policyType = policyType;
        this.basePremium = basePremium;
        this.riskLoading = riskLoading;
        this.finalPremium = finalPremium;
    }
    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public BigDecimal getBasePremium() { return basePremium; }
    public void setBasePremium(BigDecimal basePremium) { this.basePremium = basePremium; }
    public BigDecimal getRiskLoading() { return riskLoading; }
    public void setRiskLoading(BigDecimal riskLoading) { this.riskLoading = riskLoading; }
    public BigDecimal getFinalPremium() { return finalPremium; }
    public void setFinalPremium(BigDecimal finalPremium) { this.finalPremium = finalPremium; }
}
''',
    'src/main/java/com/insurance/dto/ReportResponse.java': '''package com.insurance.dto;

public class ReportResponse {
    private String label;
    private String value;

    public ReportResponse() {}
    public ReportResponse(String label, String value) {
        this.label = label;
        this.value = value;
    }
    public String getLabel() { return label; }
    public void setLabel(String label) { this.label = label; }
    public String getValue() { return value; }
    public void setValue(String value) { this.value = value; }
}
''',
    'src/main/java/com/insurance/exception/ResourceNotFoundException.java': '''package com.insurance.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
''',
    'src/main/java/com/insurance/exception/InvalidRequestException.java': '''package com.insurance.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.BAD_REQUEST)
public class InvalidRequestException extends RuntimeException {
    public InvalidRequestException(String message) {
        super(message);
    }
}
''',
    'src/main/java/com/insurance/exception/GlobalExceptionHandler.java': '''package com.insurance.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import java.util.HashMap;
import java.util.Map;

@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<Object> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", ex.getMessage()));
    }
    @ExceptionHandler(InvalidRequestException.class)
    public ResponseEntity<Object> handleBadRequest(InvalidRequestException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", ex.getMessage()));
    }
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Object> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach(error -> {
            String field = ((FieldError) error).getField();
            String message = error.getDefaultMessage();
            errors.put(field, message);
        });
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errors);
    }
}
''',
    'src/main/java/com/insurance/service/PremiumCalculator.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;

public interface PremiumCalculator {
    PremiumResponse calculatePremium(PremiumRequest request);
}
''',
    'src/main/java/com/insurance/service/LifeInsurancePremiumCalculator.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("LIFE")
public class LifeInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.02));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getAge() != null && request.getAge() > 45) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        if (Boolean.TRUE.equals(request.getSmoker())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.25)));
        }
        if (request.getSumInsured().compareTo(BigDecimal.valueOf(1000000)) > 0) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.10)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
''',
    'src/main/java/com/insurance/service/HealthInsurancePremiumCalculator.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("HEALTH")
public class HealthInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.03));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getAge() != null && request.getAge() > 50) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.30)));
        }
        if (Boolean.TRUE.equals(request.getPreExistingDisease())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.25)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
''',
    'src/main/java/com/insurance/service/VehicleInsurancePremiumCalculator.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("VEHICLE")
public class VehicleInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.04));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getVehicleAge() != null && request.getVehicleAge() > 5) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.15)));
        }
        if (Boolean.TRUE.equals(request.getAccidentHistory())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
''',
    'src/main/java/com/insurance/service/PropertyInsurancePremiumCalculator.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import org.springframework.stereotype.Component;
import java.math.BigDecimal;

@Component("PROPERTY")
public class PropertyInsurancePremiumCalculator implements PremiumCalculator {
    @Override
    public PremiumResponse calculatePremium(PremiumRequest request) {
        BigDecimal basePremium = request.getSumInsured().multiply(BigDecimal.valueOf(0.015));
        BigDecimal loading = BigDecimal.ZERO;
        if (request.getPropertyAge() != null && request.getPropertyAge() > 10) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.10)));
        }
        if (Boolean.TRUE.equals(request.getHighRiskLocation())) {
            loading = loading.add(basePremium.multiply(BigDecimal.valueOf(0.20)));
        }
        BigDecimal finalPremium = basePremium.add(loading);
        return new PremiumResponse(request.getPolicyType(), basePremium, loading, finalPremium);
    }
}
''',
    'src/main/java/com/insurance/service/PremiumCalculationService.java': '''package com.insurance.service;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.exception.InvalidRequestException;
import org.springframework.stereotype.Service;
import java.util.Map;

@Service
public class PremiumCalculationService {
    private final Map<String, PremiumCalculator> calculators;

    public PremiumCalculationService(Map<String, PremiumCalculator> calculators) {
        this.calculators = calculators;
    }

    public PremiumResponse calculatePremium(PremiumRequest request) {
        if (request.getPolicyType() == null || request.getPolicyType().isBlank()) {
            throw new InvalidRequestException("Policy type is required");
        }
        PremiumCalculator calculator = calculators.get(request.getPolicyType().toUpperCase());
        if (calculator == null) {
            throw new InvalidRequestException("Unsupported policy type: " + request.getPolicyType());
        }
        return calculator.calculatePremium(request);
    }
}
''',
    'src/main/java/com/insurance/service/CustomerService.java': '''package com.insurance.service;

import com.insurance.dto.CustomerRequest;
import com.insurance.entity.Customer;
import com.insurance.entity.User;
import com.insurance.exception.InvalidRequestException;
import com.insurance.exception.ResourceNotFoundException;
import com.insurance.repository.CustomerRepository;
import com.insurance.repository.UserRepository;
import org.springframework.stereotype.Service;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.util.List;

@Service
public class CustomerService {
    private final UserRepository userRepository;
    private final CustomerRepository customerRepository;

    public CustomerService(UserRepository userRepository, CustomerRepository customerRepository) {
        this.userRepository = userRepository;
        this.customerRepository = customerRepository;
    }

    public Customer registerCustomer(CustomerRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new InvalidRequestException("Email already exists");
        }
        User user = new User();
        user.setFullName(request.getFullName());
        user.setEmail(request.getEmail());
        user.setPassword(request.getPassword());
        user.setRole(request.getRole());
        user = userRepository.save(user);

        Customer customer = new Customer();
        customer.setUser(user);
        customer.setPhone(request.getPhone());
        try {
            customer.setDateOfBirth(LocalDate.parse(request.getDateOfBirth()));
        } catch (DateTimeParseException ex) {
            throw new InvalidRequestException("Invalid dateOfBirth format. Expected yyyy-MM-dd");
        }
        customer.setGender(request.getGender());
        customer.setAddress(request.getAddress());
        return customerRepository.save(customer);
    }

    public Customer getCustomer(Long id) {
        return customerRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found"));
    }

    public Customer updateCustomer(Long id, CustomerRequest request) {
        Customer existing = getCustomer(id);
        existing.setPhone(request.getPhone());
        existing.setGender(request.getGender());
        existing.setAddress(request.getAddress());
        return customerRepository.save(existing);
    }

    public List<Customer> findAllCustomers() {
        return customerRepository.findAll();
    }
}
''',
    'src/main/java/com/insurance/service/PolicyService.java': '''package com.insurance.service;

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
        premiumRequest.setAge(30);
        premiumRequest.setSumInsured(request.getSumInsured());
        PremiumResponse premiumResponse = premiumCalculationService.calculatePremium(premiumRequest);
        policy.setPremiumAmount(premiumResponse.getFinalPremium());
        return policyRepository.save(policy);
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
''',
    'src/main/java/com/insurance/service/ClaimService.java': '''package com.insurance.service;

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
''',
    'src/main/java/com/insurance/service/ReportService.java': '''package com.insurance.service;

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
''',
    'src/main/java/com/insurance/controller/CustomerController.java': '''package com.insurance.controller;

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
''',
    'src/main/java/com/insurance/controller/PolicyController.java': '''package com.insurance.controller;

import com.insurance.dto.PolicyRequest;
import com.insurance.entity.Policy;
import com.insurance.service.PolicyService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/policies")
public class PolicyController {
    private final PolicyService policyService;

    public PolicyController(PolicyService policyService) {
        this.policyService = policyService;
    }

    @PostMapping
    public ResponseEntity<Policy> createPolicy(@Valid @RequestBody PolicyRequest request) {
        return ResponseEntity.ok(policyService.createPolicy(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Policy> getPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.getPolicy(id));
    }

    @GetMapping
    public ResponseEntity<List<Policy>> getAllPolicies() {
        return ResponseEntity.ok(policyService.getAllPolicies());
    }

    @PutMapping("/{id}/approve")
    public ResponseEntity<Policy> approvePolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.approvePolicy(id));
    }

    @PutMapping("/{id}/reject")
    public ResponseEntity<Policy> rejectPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.rejectPolicy(id));
    }

    @PutMapping("/{id}/cancel")
    public ResponseEntity<Policy> cancelPolicy(@PathVariable Long id) {
        return ResponseEntity.ok(policyService.cancelPolicy(id));
    }

    @GetMapping("/active")
    public ResponseEntity<List<Policy>> getActivePolicies() {
        return ResponseEntity.ok(policyService.getActivePolicies());
    }

    @GetMapping("/expiring-soon")
    public ResponseEntity<List<Policy>> getExpiringSoonPolicies() {
        return ResponseEntity.ok(policyService.getExpiringSoonPolicies());
    }
}
''',
    'src/main/java/com/insurance/controller/ClaimController.java': '''package com.insurance.controller;

import com.insurance.dto.ClaimRequest;
import com.insurance.entity.Claim;
import com.insurance.service.ClaimService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/claims")
public class ClaimController {
    private final ClaimService claimService;

    public ClaimController(ClaimService claimService) {
        this.claimService = claimService;
    }

    @PostMapping
    public ResponseEntity<Claim> submitClaim(@Valid @RequestBody ClaimRequest request) {
        return ResponseEntity.ok(claimService.submitClaim(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Claim> getClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.getClaim(id));
    }

    @GetMapping
    public ResponseEntity<List<Claim>> getAllClaims() {
        return ResponseEntity.ok(claimService.getAllClaims());
    }

    @PutMapping("/{id}/under-review")
    public ResponseEntity<Claim> reviewClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.reviewClaim(id));
    }

    @PutMapping("/{id}/approve")
    public ResponseEntity<Claim> approveClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.approveClaim(id));
    }

    @PutMapping("/{id}/reject")
    public ResponseEntity<Claim> rejectClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.rejectClaim(id));
    }

    @PutMapping("/{id}/settle")
    public ResponseEntity<Claim> settleClaim(@PathVariable Long id) {
        return ResponseEntity.ok(claimService.settleClaim(id));
    }

    @GetMapping("/status/{status}")
    public ResponseEntity<List<Claim>> getClaimsByStatus(@PathVariable String status) {
        return ResponseEntity.ok(claimService.getClaimsByStatus(status.toUpperCase()));
    }
}
''',
    'src/main/java/com/insurance/controller/PremiumController.java': '''package com.insurance.controller;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.PremiumCalculationService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/premium")
public class PremiumController {
    private final PremiumCalculationService premiumCalculationService;

    public PremiumController(PremiumCalculationService premiumCalculationService) {
        this.premiumCalculationService = premiumCalculationService;
    }

    @PostMapping("/calculate")
    public ResponseEntity<PremiumResponse> calculate(@Valid @RequestBody PremiumRequest request) {
        return ResponseEntity.ok(premiumCalculationService.calculatePremium(request));
    }
}
''',
    'src/main/java/com/insurance/controller/ReportController.java': '''package com.insurance.controller;

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
''',
    'src/main/java/com/insurance/config/SoapConfig.java': '''package com.insurance.config;

import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.ws.config.annotation.EnableWs;
import org.springframework.ws.transport.http.MessageDispatcherServlet;
import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;
import org.springframework.xml.xsd.SimpleXsdSchema;
import org.springframework.xml.xsd.XsdSchema;

@EnableWs
@Configuration
public class SoapConfig {
    @Bean
    public ServletRegistrationBean<MessageDispatcherServlet> messageDispatcherServlet(ApplicationContext context) {
        MessageDispatcherServlet servlet = new MessageDispatcherServlet();
        servlet.setApplicationContext(context);
        servlet.setTransformWsdlLocations(true);
        return new ServletRegistrationBean<>(servlet, "/soap/*");
    }

    @Bean(name = "premiumCalculator")
    public DefaultWsdl11Definition defaultWsdl11Definition(XsdSchema premiumSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("PremiumCalculatorPort");
        wsdl11Definition.setLocationUri("/soap");
        wsdl11Definition.setTargetNamespace("http://insurance.com/soap");
        wsdl11Definition.setSchema(premiumSchema);
        return wsdl11Definition;
    }

    @Bean
    public XsdSchema premiumSchema() {
        return new SimpleXsdSchema(new ClassPathResource("premium.xsd"));
    }
}
''',
    'src/main/java/com/insurance/soap/CalculatePremiumRequest.java': '''package com.insurance.soap;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlRootElement;
import jakarta.xml.bind.annotation.XmlType;
import java.math.BigDecimal;

@XmlRootElement(name = "calculatePremiumRequest", namespace = "http://insurance.com/soap")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "calculatePremiumRequest", propOrder = {"policyType", "age", "sumInsured", "smoker", "preExistingDisease", "vehicleAge", "accidentHistory", "propertyAge", "highRiskLocation"})
public class CalculatePremiumRequest {
    private String policyType;
    private Integer age;
    private BigDecimal sumInsured;
    private boolean smoker;
    private boolean preExistingDisease;
    private Integer vehicleAge;
    private boolean accidentHistory;
    private Integer propertyAge;
    private boolean highRiskLocation;

    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
    public BigDecimal getSumInsured() { return sumInsured; }
    public void setSumInsured(BigDecimal sumInsured) { this.sumInsured = sumInsured; }
    public boolean isSmoker() { return smoker; }
    public void setSmoker(boolean smoker) { this.smoker = smoker; }
    public boolean isPreExistingDisease() { return preExistingDisease; }
    public void setPreExistingDisease(boolean preExistingDisease) { this.preExistingDisease = preExistingDisease; }
    public Integer getVehicleAge() { return vehicleAge; }
    public void setVehicleAge(Integer vehicleAge) { this.vehicleAge = vehicleAge; }
    public boolean isAccidentHistory() { return accidentHistory; }
    public void setAccidentHistory(boolean accidentHistory) { this.accidentHistory = accidentHistory; }
    public Integer getPropertyAge() { return propertyAge; }
    public void setPropertyAge(Integer propertyAge) { this.propertyAge = propertyAge; }
    public boolean isHighRiskLocation() { return highRiskLocation; }
    public void setHighRiskLocation(boolean highRiskLocation) { this.highRiskLocation = highRiskLocation; }
}
''',
    'src/main/java/com/insurance/soap/CalculatePremiumResponse.java': '''package com.insurance.soap;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlRootElement;
import jakarta.xml.bind.annotation.XmlType;
import java.math.BigDecimal;

@XmlRootElement(name = "calculatePremiumResponse", namespace = "http://insurance.com/soap")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "calculatePremiumResponse", propOrder = {"policyType", "basePremium", "riskLoading", "finalPremium"})
public class CalculatePremiumResponse {
    private String policyType;
    private BigDecimal basePremium;
    private BigDecimal riskLoading;
    private BigDecimal finalPremium;

    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
    public BigDecimal getBasePremium() { return basePremium; }
    public void setBasePremium(BigDecimal basePremium) { this.basePremium = basePremium; }
    public BigDecimal getRiskLoading() { return riskLoading; }
    public void setRiskLoading(BigDecimal riskLoading) { this.riskLoading = riskLoading; }
    public BigDecimal getFinalPremium() { return finalPremium; }
    public void setFinalPremium(BigDecimal finalPremium) { this.finalPremium = finalPremium; }
}
''',
    'src/main/java/com/insurance/soap/PremiumEndpoint.java': '''package com.insurance.soap;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.PremiumCalculationService;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

@Endpoint
public class PremiumEndpoint {
    private static final String NAMESPACE_URI = "http://insurance.com/soap";
    private final PremiumCalculationService premiumCalculationService;

    public PremiumEndpoint(PremiumCalculationService premiumCalculationService) {
        this.premiumCalculationService = premiumCalculationService;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "calculatePremiumRequest")
    @ResponsePayload
    public CalculatePremiumResponse calculatePremium(@RequestPayload CalculatePremiumRequest request) {
        PremiumRequest premiumRequest = new PremiumRequest();
        premiumRequest.setPolicyType(request.getPolicyType());
        premiumRequest.setAge(request.getAge());
        premiumRequest.setSumInsured(request.getSumInsured());
        premiumRequest.setSmoker(request.isSmoker());
        premiumRequest.setPreExistingDisease(request.isPreExistingDisease());
        premiumRequest.setVehicleAge(request.getVehicleAge());
        premiumRequest.setAccidentHistory(request.isAccidentHistory());
        premiumRequest.setPropertyAge(request.getPropertyAge());
        premiumRequest.setHighRiskLocation(request.isHighRiskLocation());

        PremiumResponse response = premiumCalculationService.calculatePremium(premiumRequest);
        CalculatePremiumResponse soapResponse = new CalculatePremiumResponse();
        soapResponse.setPolicyType(response.getPolicyType());
        soapResponse.setBasePremium(response.getBasePremium());
        soapResponse.setRiskLoading(response.getRiskLoading());
        soapResponse.setFinalPremium(response.getFinalPremium());
        return soapResponse;
    }
}
''',
    'src/main/resources/static/index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Insurance Portal</title>
    <link rel="stylesheet" href="/css/styles.css" />
</head>
<body>
    <div class="container">
        <h1>Insurance Policy & Claims System</h1>
        <p>Use the links below to access registration, premium calculator, claim submission, and admin dashboards.</p>
        <nav>
            <ul>
                <li><a href="/register.html">Customer Registration</a></li>
                <li><a href="/premium-calculator.html">Premium Calculator</a></li>
                <li><a href="/claim-submission.html">Claim Submission</a></li>
                <li><a href="/admin-dashboard.html">Admin Dashboard</a></li>
                <li><a href="/swagger-ui.html">Swagger API Docs</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>
''',
    'src/main/resources/static/register.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Register Customer</title>
    <link rel="stylesheet" href="/css/styles.css" />
    <script src="/js/register.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Customer Registration</h1>
        <form id="registrationForm">
            <label>Full Name<input type="text" name="fullName" required></label>
            <label>Email<input type="email" name="email" required></label>
            <label>Password<input type="password" name="password" required></label>
            <label>Role<select name="role"><option>CUSTOMER</option><option>AGENT</option></select></label>
            <label>Phone<input type="text" name="phone" required></label>
            <label>Date of Birth<input type="date" name="dateOfBirth" required></label>
            <label>Gender<select name="gender"><option>Male</option><option>Female</option><option>Other</option></select></label>
            <label>Address<textarea name="address" required></textarea></label>
            <button type="submit">Register</button>
        </form>
        <div id="message"></div>
    </div>
</body>
</html>
''',
    'src/main/resources/static/premium-calculator.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Premium Calculator</title>
    <link rel="stylesheet" href="/css/styles.css" />
    <script src="/js/premium.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Premium Calculator</h1>
        <form id="premiumForm">
            <label>Policy Type<select name="policyType"><option>LIFE</option><option>HEALTH</option><option>VEHICLE</option><option>PROPERTY</option></select></label>
            <label>Age<input type="number" name="age" required></label>
            <label>Sum Insured<input type="number" name="sumInsured" required></label>
            <label><input type="checkbox" name="smoker"> Smoker</label>
            <label><input type="checkbox" name="preExistingDisease"> Pre-existing Disease</label>
            <label>Vehicle Age<input type="number" name="vehicleAge"></label>
            <label><input type="checkbox" name="accidentHistory"> Accident History</label>
            <label>Property Age<input type="number" name="propertyAge"></label>
            <label><input type="checkbox" name="highRiskLocation"> High Risk Location</label>
            <button type="submit">Calculate Premium</button>
        </form>
        <div id="result"></div>
    </div>
</body>
</html>
''',
    'src/main/resources/static/claim-submission.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Claim Submission</title>
    <link rel="stylesheet" href="/css/styles.css" />
    <script src="/js/claim.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Submit a Claim</h1>
        <form id="claimForm">
            <label>Policy ID<input type="number" name="policyId" required></label>
            <label>Customer ID<input type="number" name="customerId" required></label>
            <label>Claim Amount<input type="number" step="0.01" name="claimAmount" required></label>
            <label>Reason<textarea name="claimReason" required></textarea></label>
            <button type="submit">Submit Claim</button>
        </form>
        <div id="claimMessage"></div>
    </div>
</body>
</html>
''',
    'src/main/resources/static/admin-dashboard.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="/css/styles.css" />
    <script src="/js/admin.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Admin Dashboard</h1>
        <button id="loadReports">Load Reports</button>
        <div id="reports"></div>
    </div>
</body>
</html>
''',
    'src/main/resources/static/css/styles.css': '''body { font-family: Arial, sans-serif; background: #f4f7fb; margin: 0; padding: 0; }
.container { max-width: 760px; margin: 40px auto; background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08); }
h1 { margin-top: 0; }
form label { display: block; margin-bottom: 12px; }
form input, form textarea, form select { width: 100%; padding: 10px; margin-top: 6px; border: 1px solid #cbd5e1; border-radius: 4px; }
button { padding: 12px 18px; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
button:hover { background: #1d4ed8; }
#result, #message, #claimMessage, #reports { margin-top: 16px; }
nav ul { padding-left: 0; list-style: none; }
nav li { margin-bottom: 10px; }
nav a { color: #2563eb; text-decoration: none; }
''',
    'src/main/resources/static/js/register.js': '''const registrationForm = document.getElementById('registrationForm');
registrationForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(registrationForm);
    const payload = Object.fromEntries(formData.entries());
    const response = await fetch('/api/customers/register', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const message = document.getElementById('message');
    if (response.ok) {
        message.textContent = 'Registration successful. Customer created.';
    } else {
        const body = await response.json();
        message.textContent = body.error || JSON.stringify(body);
    }
});
''',
    'src/main/resources/static/js/premium.js': '''const premiumForm = document.getElementById('premiumForm');
premiumForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(premiumForm);
    const payload = {
        policyType: formData.get('policyType'),
        age: Number(formData.get('age')),
        sumInsured: Number(formData.get('sumInsured')),
        smoker: formData.get('smoker') === 'on',
        preExistingDisease: formData.get('preExistingDisease') === 'on',
        vehicleAge: Number(formData.get('vehicleAge')) || 0,
        accidentHistory: formData.get('accidentHistory') === 'on',
        propertyAge: Number(formData.get('propertyAge')) || 0,
        highRiskLocation: formData.get('highRiskLocation') === 'on'
    };
    const response = await fetch('/api/premium/calculate', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const result = document.getElementById('result');
    if (response.ok) {
        const data = await response.json();
        result.innerHTML = `<strong>Policy Type:</strong> ${data.policyType}<br><strong>Base Premium:</strong> ${data.basePremium}<br><strong>Risk Loading:</strong> ${data.riskLoading}<br><strong>Final Premium:</strong> ${data.finalPremium}`;
    } else {
        const body = await response.json();
        result.textContent = body.error || JSON.stringify(body);
    }
});
''',
    'src/main/resources/static/js/claim.js': '''const claimForm = document.getElementById('claimForm');
claimForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(claimForm);
    const payload = {
        policyId: Number(formData.get('policyId')),
        customerId: Number(formData.get('customerId')),
        claimAmount: Number(formData.get('claimAmount')),
        claimReason: formData.get('claimReason')
    };
    const response = await fetch('/api/claims', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)
    });
    const message = document.getElementById('claimMessage');
    if (response.ok) {
        message.textContent = 'Claim submitted successfully.';
    } else {
        const body = await response.json();
        message.textContent = body.error || JSON.stringify(body);
    }
});
''',
    'src/main/resources/static/js/admin.js': '''const loadReports = document.getElementById('loadReports');
loadReports?.addEventListener('click', async () => {
    const sections = [
        {title: 'Active Policies', path: '/api/reports/active-policies'},
        {title: 'Pending Claims', path: '/api/reports/pending-claims'},
        {title: 'Approved Claims', path: '/api/reports/approved-claims'},
        {title: 'Rejected Claims', path: '/api/reports/rejected-claims'},
        {title: 'Monthly Premium', path: '/api/reports/monthly-premium'},
        {title: 'Claims by Policy Type', path: '/api/reports/claims-by-policy-type'},
        {title: 'Expiring Soon Policies', path: '/api/reports/expiring-soon'},
        {title: 'Customers with Multiple Policies', path: '/api/reports/customers-multiple-policies'}
    ];
    const container = document.getElementById('reports');
    container.innerHTML = '';
    for (const section of sections) {
        const response = await fetch(section.path);
        const data = await response.json();
        const sectionDiv = document.createElement('div');
        sectionDiv.innerHTML = `<h2>${section.title}</h2><pre>${JSON.stringify(data, null, 2)}</pre>`;
        container.appendChild(sectionDiv);
    }
});
''',
    'src/test/java/com/insurance/PremiumCalculationServiceTest.java': '''package com.insurance;

import com.insurance.dto.PremiumRequest;
import com.insurance.dto.PremiumResponse;
import com.insurance.service.PremiumCalculationService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.GenericApplicationContext;
import java.math.BigDecimal;
import static org.junit.jupiter.api.Assertions.*;

public class PremiumCalculationServiceTest {
    private PremiumCalculationService service;

    @BeforeEach
    public void setup() {
        GenericApplicationContext context = new AnnotationConfigApplicationContext("com.insurance.service");
        service = context.getBean(PremiumCalculationService.class);
    }

    @Test
    public void testLifeInsurancePremiumForSmokerAbove45() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("LIFE");
        request.setAge(48);
        request.setSumInsured(BigDecimal.valueOf(1000000));
        request.setSmoker(true);
        PremiumResponse response = service.calculatePremium(request);
        assertNotNull(response);
        assertEquals("LIFE", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }

    @Test
    public void testHealthInsurancePremiumWithPreExistingDisease() {
        PremiumRequest request = new PremiumRequest();
        request.setPolicyType("HEALTH");
        request.setAge(55);
        request.setSumInsured(BigDecimal.valueOf(500000));
        request.setPreExistingDisease(true);
        PremiumResponse response = service.calculatePremium(request);
        assertEquals("HEALTH", response.getPolicyType());
        assertTrue(response.getFinalPremium().compareTo(response.getBasePremium()) > 0);
    }
}
''',
    'src/test/java/com/insurance/PolicyServiceTest.java': '''package com.insurance;

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
''',
    'src/test/java/com/insurance/ClaimServiceTest.java': '''package com.insurance;

import com.insurance.dto.ClaimRequest;
import com.insurance.entity.Claim;
import com.insurance.entity.Customer;
import com.insurance.entity.Policy;
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
}
''',
    'README.md': '''# Insurance Policy & Claims Management System

## Overview
A Java Spring Boot insurance management system that supports customer registration, policy lifecycle, premium calculations, claims workflows, SQL-based reporting, REST APIs, and SOAP premium service.

## Features
- Customer registration and profile management
- Policy creation, approval, rejection, cancellation, expiring soon reports
- Premium calculation for Life, Health, Vehicle, Property policies
- Claim submission, review, approval, rejection, settlement
- Report APIs for active policies, pending claims, monthly premium, claims by type
- Swagger API documentation
- SOAP web service for premium calculation
- Unit tests with JUnit and Mockito

## Tech Stack
- Java 17
- Spring Boot
- Spring Data JPA
- Spring Web and Spring Web Services
- H2 in-memory database for local demo
- Maven
- Swagger/OpenAPI
- HTML/CSS/JavaScript frontend

## Run Locally
1. Build: `mvn clean package`
2. Start: `mvn spring-boot:run`
3. Access:
   - Swagger: http://localhost:8080/swagger-ui.html
   - H2 Console: http://localhost:8080/h2-console
   - Frontend: http://localhost:8080/index.html

## SOAP Endpoint
Base SOAP location: http://localhost:8080/soap/premiumCalculator.wsdl

## Notes
This project uses layered architecture with controllers, services, repositories, DTOs, and SOAP integration.
''',
    'API_DOCUMENTATION.md': '''# API Documentation

## Customer APIs
- POST /api/customers/register
- GET /api/customers/{id}
- PUT /api/customers/{id}
- GET /api/customers/{id}/policies
- GET /api/customers/{id}/claims

## Policy APIs
- POST /api/policies
- GET /api/policies/{id}
- GET /api/policies
- PUT /api/policies/{id}/approve
- PUT /api/policies/{id}/reject
- PUT /api/policies/{id}/cancel
- GET /api/policies/active
- GET /api/policies/expiring-soon

## Premium APIs
- POST /api/premium/calculate

## Claim APIs
- POST /api/claims
- GET /api/claims/{id}
- GET /api/claims
- PUT /api/claims/{id}/under-review
- PUT /api/claims/{id}/approve
- PUT /api/claims/{id}/reject
- PUT /api/claims/{id}/settle
- GET /api/claims/status/{status}

## Report APIs
- GET /api/reports/active-policies
- GET /api/reports/pending-claims
- GET /api/reports/approved-claims
- GET /api/reports/rejected-claims
- GET /api/reports/monthly-premium
- GET /api/reports/claims-by-policy-type
- GET /api/reports/expiring-soon
- GET /api/reports/customers-multiple-policies
''',
    'DATABASE_SCHEMA.md': '''# Database Schema

## users
- user_id BIGSERIAL PRIMARY KEY
- full_name VARCHAR(100)
- email VARCHAR(100) UNIQUE
- password VARCHAR(255)
- role VARCHAR(20)
- created_at TIMESTAMP

## customers
- customer_id BIGSERIAL PRIMARY KEY
- user_id BIGINT REFERENCES users(user_id)
- phone VARCHAR(15)
- date_of_birth DATE
- gender VARCHAR(10)
- address TEXT
- created_at TIMESTAMP

## policies
- policy_id BIGSERIAL PRIMARY KEY
- customer_id BIGINT REFERENCES customers(customer_id)
- policy_type VARCHAR(30)
- sum_insured DECIMAL(12,2)
- premium_amount DECIMAL(12,2)
- start_date DATE
- end_date DATE
- status VARCHAR(30)
- created_at TIMESTAMP

## claims
- claim_id BIGSERIAL PRIMARY KEY
- policy_id BIGINT REFERENCES policies(policy_id)
- customer_id BIGINT REFERENCES customers(customer_id)
- claim_amount DECIMAL(12,2)
- claim_reason TEXT
- claim_status VARCHAR(30)
- admin_remarks TEXT
- created_at TIMESTAMP
- updated_at TIMESTAMP

## payments
- payment_id BIGSERIAL PRIMARY KEY
- policy_id BIGINT REFERENCES policies(policy_id)
- customer_id BIGINT REFERENCES customers(customer_id)
- amount DECIMAL(12,2)
- payment_status VARCHAR(30)
- payment_date TIMESTAMP
''',
    'TEST_CASES.md': '''# Test Cases

## PremiumCalculationServiceTest
- Life insurance premium for smoker above 45
- Health insurance premium with pre-existing disease
- Vehicle insurance premium with accident history
- Property insurance premium in high-risk location
- Invalid policy type should return error

## PolicyServiceTest
- Create valid policy request
- Reject policy with invalid dates
- Approve pending policy
- Cancel active policy
- Prevent policy creation with zero sum insured

## ClaimServiceTest
- Submit claim for active policy
- Reject claim for expired or inactive policy
- Approve claim under valid conditions
- Reject claim if claim amount exceeds sum insured
- Settle only approved claims
''',
    'SOAP_SERVICE_DOCUMENTATION.md': '''# SOAP Service Documentation

## Service
PremiumCalculatorSoapService

## Operation
calculatePremium

## Request Example
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ins="http://insurance.com/soap">
   <soapenv:Header/>
   <soapenv:Body>
      <ins:calculatePremiumRequest>
         <ins:policyType>LIFE</ins:policyType>
         <ins:age>48</ins:age>
         <ins:sumInsured>1000000</ins:sumInsured>
         <ins:smoker>true</ins:smoker>
         <ins:preExistingDisease>false</ins:preExistingDisease>
         <ins:vehicleAge>0</ins:vehicleAge>
         <ins:accidentHistory>false</ins:accidentHistory>
         <ins:propertyAge>0</ins:propertyAge>
         <ins:highRiskLocation>false</ins:highRiskLocation>
      </ins:calculatePremiumRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

## Response Example
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ins="http://insurance.com/soap">
   <soapenv:Body>
      <ins:calculatePremiumResponse>
         <ins:policyType>LIFE</ins:policyType>
         <ins:basePremium>20000</ins:basePremium>
         <ins:riskLoading>9000</ins:riskLoading>
         <ins:finalPremium>29000</ins:finalPremium>
      </ins:calculatePremiumResponse>
   </soapenv:Body>
</soapenv:Envelope>
```
'''
}

for rel_path, content in files.items():
    file_path = root / rel_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding='utf-8')

print('Created', len(files), 'files in', root)
