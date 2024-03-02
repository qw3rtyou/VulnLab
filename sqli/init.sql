CREATE DATABASE IF NOT EXISTS sqli_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sqli_lab;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- 한글지원

INSERT INTO user (username, password) VALUES ('guest', 'password');
INSERT INTO user (username, password) VALUES ('admin', 'KO{4dm1n_1s_vUln3r4bl3}'); -- 환경변수 처리해야 됨

CREATE TABLE IF NOT EXISTS `KO{` (
    `Und3r_c0` VARCHAR(255) NOT NULL
);

INSERT INTO `KO{` (`Und3r_c0`) VALUES ('nstrUct10n');
