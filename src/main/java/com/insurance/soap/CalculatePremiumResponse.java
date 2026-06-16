package com.insurance.soap;

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
