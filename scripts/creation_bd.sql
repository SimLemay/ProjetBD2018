DROP DATABASE IF EXISTS ProjetBD;
CREATE DATABASE ProjetBD CHARACTER SET utf8;
DROP USER IF EXISTS 'projetbduser'@'localhost';
CREATE USER 'projetbduser'@'localhost' IDENTIFIED BY 'gUPqV1qOGG4jVcn4Ab8uuPeiCV42Pm4N4Eh1hJ7SUVctzeH7cbep1EMRUVmUGNnv';
GRANT ALL PRIVILEGES ON ProjetBD.* To 'projetbduser'@'localhost';