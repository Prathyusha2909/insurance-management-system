# Database Schema

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
