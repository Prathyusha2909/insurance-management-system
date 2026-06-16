package com.insurance.dto;

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
