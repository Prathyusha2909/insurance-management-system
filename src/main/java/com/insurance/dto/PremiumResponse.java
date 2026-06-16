package com.insurance.dto;

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
