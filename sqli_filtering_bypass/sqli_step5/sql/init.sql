CREATE DATABASE IF NOT EXISTS sqli_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sqli_lab;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- 한글지원

INSERT INTO user (username, password) VALUES ('guest', 'password');
INSERT INTO user (username, password) VALUES ('admin', 'K0{good_4ft3rn00n!}'); -- 환경변수 처리해야 됨


