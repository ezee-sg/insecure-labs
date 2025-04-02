-- init.sql
CREATE DATABASE IF NOT EXISTS eventos;
USE eventos;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    evento_id INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (evento_id) REFERENCES eventos(id)
);

CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    factura_id INT NOT NULL,
    evento_id INT NOT NULL,
    FOREIGN KEY (factura_id) REFERENCES facturas(id),
    FOREIGN KEY (evento_id) REFERENCES eventos(id)
);

INSERT INTO eventos (nombre) VALUES
('Concierto de Rock'),
('Feria de Tecnologia'),
('Conferencia de Seguridad Informatica'),
('Taller de Programacion'),
('Exposicion de Arte');


INSERT INTO users (username, password) VALUES
('luis', 'password1'),
('maria', 'password2'),
('lucas', 'password3');

INSERT INTO facturas (id, user_id, evento_id, cantidad) VALUES
(10, 1, 2, 3),
(45, 2, 4, 10),
(112, 3, 1, 5);

INSERT INTO tickets (factura_id, evento_id) VALUES
(10, 2),
(10, 2),
(10, 2),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(45, 4),
(112, 1),
(112, 1),
(112, 1),
(112, 1),
(112, 1);
