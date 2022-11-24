-- creates database and user for the omni project
CREATE DATABASE IF NOT EXISTS omni;
CREATE USER IF NOT EXISTS 'omni_user'@'localhost' IDENTIFIED BY 'omni_pwd';
GRANT ALL PRIVILEGES ON `omni`.*  TO 'omni_user'@'localhost';
FLUSH PRIVILEGES;