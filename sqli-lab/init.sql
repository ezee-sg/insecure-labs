CREATE DATABASE IF NOT EXISTS shop;
USE shop;

-- Tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Insertar algunos productos
INSERT INTO products (name, price) VALUES
('Laptop Hacker', 999.99),
('USB Rubber Ducky', 49.99),
('WiFi Pineapple', 199.99),
('Raspberry Pi', 59.99),
('Lockpick Set', 29.99);

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insertar usuarios
INSERT INTO users (username, password) VALUES
('admin', 'admin123$!'),
('paco', 'megustanlasbasesdedatos'),
('alberto', 'alberto_1980');
