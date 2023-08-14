CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  company_name VARCHAR(50),
  contact_name VARCHAR(50)
);


CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  title VARCHAR(50),
  birth_date DATE,
  notes VARCHAR(50)
);


CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(customer_id),
  employee_id INTEGER REFERENCES employees(employee_id),
  order_date DATE,
  ship_sity TEXT
);


