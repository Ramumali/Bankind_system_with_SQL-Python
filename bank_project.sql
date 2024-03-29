SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
    `acno` int(11) NOT NULL AUTO_INCREMENT,
    `name` char(30) DEFAULT NULL,
    `address` varchar(50) DEFAULT NULL,
    `phone` varchar(15) DEFAULT NULL,
    `email` varchar(80) DEFAULT NULL,
    `aadhar_no` varchar(20) DEFAULT NULL,
    `acc_type` varchar(20) DEFAULT NULL,
    `status` char(15) DEFAULT NULL,
    `balance` float(15,2) DEFAULT NULL,
     PRIMARY KEY (`acno`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
INSERT INTO `customer` (`acno`,`name`,`address`,`phone`,`email`,`aadhar_no`,`acc_type`,`status`, `balance` ) VALUES
(1,'Ramanathan M','123,Hackers way','9677546385','ramumali2002@gmail.com','561541019770','saving','active', '10000.00'),
(2,'Mahalingam M','123,Shanthi Street','989736785','marmu4546@gmail.com','6895000899566','current','active', '50000.00'),
(3,'Parvathi M','63,shanmuga yogeswarar street','9488461331','parvathi@gmail.com','896859958959','savings','active', '100000.00');

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
    `tid` int(11) NOT NULL AUTO_INCREMENT,
    `dot` date DEFAULT NULL,
    `amount` int(10) DEFAULT NULL,
    `type` char(20) DEFAULT NULL,
    `acno` int(10) DEFAULT NULL,
     PRIMARY KEY(`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
 
INSERT INTO `transaction` (`tid`,`dot`,`amount`,`type`,`acno`) VALUES
(1,'2024-03-29',2000,'deposit',1),
(2,'2024-03-17',2000,'deposit',1),
(3,'2024-03-14',2000,'withdraw',2);
