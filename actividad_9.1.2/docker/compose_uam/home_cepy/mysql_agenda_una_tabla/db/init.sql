CREATE DATABASE cepy_agenda;
use cepy_agenda;
CREATE USER 'cepy_agenda'@'%' IDENTIFIED BY 'castelar';
GRANT ALL PRIVILEGES ON `cepy_agenda%`.* TO 'cepy_agenda'@'%';
#GRANT ALL PRIVILEGES ON *.* TO 'cepy_agenda'@'%';
FLUSH PRIVILEGES;

CREATE TABLE contactos(
    id int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    telefono char(9) NOT NULL UNIQUE,
    email varchar(100) NULL,
    localidad varchar(30) NULL
);