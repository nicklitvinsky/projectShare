CREATE DATABASE IF NOT EXISTS vacation_booking1;
USE vacation_booking1;

CREATE TABLE IF NOT EXISTS roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name ENUM('user', 'admin') NOT NULL
);

CREATE TABLE IF NOT EXISTS countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    role INT NOT NULL,
    FOREIGN KEY (role) REFERENCES roles(role_id)
);

CREATE TABLE IF NOT EXISTS vacations (
    vacation_id INT AUTO_INCREMENT PRIMARY KEY,
    vacation_title VARCHAR(255) NOT NULL,
    country_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 1000 AND price <= 10000),
    total_likes INT DEFAULT 0,
    img_url VARCHAR(255),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

DELIMITER //

CREATE TRIGGER before_vacation_insert
BEFORE INSERT ON vacations
FOR EACH ROW
BEGIN
    IF NEW.start_date <= NOW() THEN  
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'start_date must be greater than the current date and time';
    END IF;
   
    IF NEW.end_date <= NEW.start_date THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'end_date must be greater than start_date';
    END IF;
END //

DELIMITER ;

CREATE TABLE IF NOT EXISTS likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    vacation_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (vacation_id) REFERENCES vacations(vacation_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
