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
('Portatil', 999.99),
('USB Rubber Ducky', 49.99),
('Raspberry Pi', 59.99),
('Camara de seguridad', 199.99),
('Teclado mecanico', 120.50),
('Auriculares Bluetooth', 89.99),
('Monitor 24 pulgadas', 179.99),
('Raton ergonomico', 45.00),
('Disco duro SSD', 129.99),
('Bateria externa', 25.99),
('Cargador solar', 39.50),
('Smartwatch', 159.00),
('Camara web HD', 60.00);



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
