CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

-- Tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);

-- Insertar algunos productos
INSERT INTO productos (nombre, precio) VALUES
('Laptop Hacker', 999.99),
('USB Rubber Ducky', 49.99),
('WiFi Pineapple', 199.99),
('Raspberry Pi', 59.99),
('Lockpick Set', 29.99);

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

-- Insertar usuarios
INSERT INTO usuarios (usuario, contrasena) VALUES
('admin', 'admin123$!'),
('paco', 'megustanlasbasesdedatos'),
('alberto', 'alberto_1980');
