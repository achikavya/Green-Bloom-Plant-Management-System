CREATE DATABASE IF NOT EXISTS green_bloom_db;
USE green_bloom_db;

CREATE TABLE IF NOT EXISTS plants (
    plant_id INT PRIMARY KEY,
    plant_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price FLOAT NOT NULL,
    quantity INT NOT NULL,
    supplier_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    plant_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    total_amount FLOAT NOT NULL,
    sale_date DATE NOT NULL
);