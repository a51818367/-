/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.5.15 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `abcbank` */

DROP TABLE IF EXISTS `abcbank`;

CREATE TABLE `abcbank` (
  `account` varchar(10) DEFAULT NULL,
  `ID` varchar(20) DEFAULT NULL,
  `name` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `province` varchar(10) DEFAULT NULL,
  `street` varchar(10) DEFAULT NULL,
  `House` varchar(10) DEFAULT NULL,
  `money` decimal(20,2) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `bankname` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `abcbank` */

insert  into `abcbank`(`account`,`ID`,`name`,`password`,`country`,`province`,`street`,`House`,`money`,`type`,`bankname`) values ('1','1','1','1','1','1','1','1','1017901.00','普通卡','中国农业银行北京昌平支行'),('2','2','2','2','2','2','2','2','9900.00','白金卡','中国农业银行北京昌平支行');

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `account` varchar(10) DEFAULT NULL,
  `ID` varchar(20) DEFAULT NULL,
  `name` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `province` varchar(10) DEFAULT NULL,
  `street` varchar(10) DEFAULT NULL,
  `House` varchar(10) DEFAULT NULL,
  `money` decimal(20,2) DEFAULT NULL,
  `bankname` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `bank` */

insert  into `bank`(`account`,`ID`,`name`,`password`,`country`,`province`,`street`,`House`,`money`,`bankname`) values ('100','1','1','1','1','1','1','1','22689.90','中国工商银行北京昌平支行'),('1','2','2','1','2','2','2','2','9959202.00','中国工商银行北京昌平支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
