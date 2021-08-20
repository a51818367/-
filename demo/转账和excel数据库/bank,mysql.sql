/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `bank` (
	`zhanghao` varchar (60),
	`yue` Decimal (22),
	`xingming` varchar (60),
	`mima` varchar (60),
	`guojia` varchar (60),
	`shengfen` varchar (60),
	`jiedao` varchar (60),
	`menpaihao` varchar (60),
	`kaihuhang` varchar (60),
	`type` varchar (60)
); 
insert into `bank` (`zhanghao`, `yue`, `xingming`, `mima`, `guojia`, `shengfen`, `jiedao`, `menpaihao`, `kaihuhang`, `type`) values('12345678','68999.00','1','1','1','1','1','1','中国农业银行','白金卡');
insert into `bank` (`zhanghao`, `yue`, `xingming`, `mima`, `guojia`, `shengfen`, `jiedao`, `menpaihao`, `kaihuhang`, `type`) values('87654321','51051.00','2','2','2','2','2','2','中国农业银行','普通卡');
insert into `bank` (`zhanghao`, `yue`, `xingming`, `mima`, `guojia`, `shengfen`, `jiedao`, `menpaihao`, `kaihuhang`, `type`) values('30482683','6000.00','1','1','1','1','1','1','中国农业银行','普通卡');
