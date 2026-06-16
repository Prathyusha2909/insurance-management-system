# Insurance Policy & Claims Management System

[![Java CI](https://github.com/Prathyusha2909/insurance-management-system/actions/workflows/maven.yml/badge.svg)](https://github.com/Prathyusha2909/insurance-management-system/actions/workflows/maven.yml)

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
