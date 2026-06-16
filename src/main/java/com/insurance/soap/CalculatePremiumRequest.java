package com.insurance.soap;

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
