CREATE DATABASE IF NOT EXISTS post CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE post;

CREATE TABLE IF NOT EXISTS post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 