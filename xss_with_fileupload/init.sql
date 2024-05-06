CREATE DATABASE IF NOT EXISTS xss_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE xss_lab;

CREATE TABLE IF NOT EXISTS post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
    uploaded_image VARCHAR(255) NOT NULL
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 