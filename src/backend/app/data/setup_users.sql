CREATE DATABASE BudgetBloomberg;

\c BudgetBloomberg

CREATE TABLE users_data (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);