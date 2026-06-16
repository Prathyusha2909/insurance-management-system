package com.insurance.service;

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
