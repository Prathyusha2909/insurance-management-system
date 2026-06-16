# SOAP Service Documentation

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
