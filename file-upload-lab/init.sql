CREATE DATABASE IF NOT EXISTS social_network;
USE social_network;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    profile_pic VARCHAR(255) DEFAULT 'uploads/default.avif'
);

/*INSERT INTO users (username, password, email) 
VALUES ('admin', '$2y$10$eJfjBpJHRAI5cFzHnT5DEuCEIxjYBoENo5IEeA4LMPfGHTOzh1a1i', 'admin@example.com');*/
