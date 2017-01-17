-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: localhost    Database: DbMysql17
-- ------------------------------------------------------
-- Server version	5.5.35-1ubuntu1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Addr`
--

DROP TABLE IF EXISTS `Addr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Addr` (
  `idAddr` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `street` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `house_number` int(11) DEFAULT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  PRIMARY KEY (`idAddr`),
  UNIQUE KEY `idAddresses_UNIQUE` (`idAddr`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Addr`
--

LOCK TABLES `Addr` WRITE;
/*!40000 ALTER TABLE `Addr` DISABLE KEYS */;
INSERT INTO `Addr` VALUES (4,NULL,NULL,NULL,32.0753439,34.77529),(5,'Tel Aviv-Yafo','Rabbi Akiva',18,32.0696336,34.7695327),(6,NULL,NULL,NULL,32.0705485,34.7919422),(7,'Tel Aviv-Yafo','Carlebach',25,32.0685503,34.7829236),(8,'Tel Aviv-Yafo','Ben Yehuda',147,32.087664,34.7731046),(9,'Tel Aviv-Yafo','Dizengoff',128,32.081489,34.774018),(10,NULL,' Salomon',9,32.061468,34.779977),(11,'Tel Aviv-Yafo','Ben Yehuda',169,32.0894897,34.7736499),(12,'Tel Aviv-Yafo',NULL,NULL,32.071478,34.7794),(13,'Tel Aviv-Yafo',NULL,NULL,32.0592808,34.7737397),(14,'Tel Aviv-Yafo','Arlozorov',NULL,32.0868253,34.7750092),(15,'Tel Aviv-Yafo','Basel',37,32.0899341,34.7804404),(16,NULL,NULL,NULL,32.1121634,34.7946168),(17,'Tel Aviv-Yafo',NULL,NULL,32.063452,34.772863),(18,'Tel Aviv-Yafo','Yigal Alon',159,32.078598,34.797902),(19,NULL,NULL,NULL,32.101457,34.775448),(20,'Tel Aviv-Yafo','Dizengoff',267,32.0949741,34.7762863),(21,'Tel Aviv-Yafo',' Allenby',118,32.063283,34.7729743),(22,'Tel Aviv-Yafo',NULL,NULL,32.0671464,34.7851945),(23,'Tel Aviv-Yafo','Frishman',16,32.0798079,34.7693701),(24,NULL,NULL,NULL,32.0706579,34.7869387),(25,'Tel Aviv-Yafo','Ben Yehuda',182,32.0882139,34.7736973),(26,'Tel Aviv-Yafo','Dizengoff',92,32.077535,34.7745664),(27,'Tel Aviv-Yafo',NULL,NULL,32.0638792,34.779878),(28,NULL,NULL,NULL,32.0793439,34.7687729),(29,NULL,NULL,NULL,32.061312,34.7599054),(30,NULL,NULL,NULL,32.0987256,34.7740058),(31,'Tel Aviv-Yafo','Rabbi Yohanan',8,32.0526408,34.7561422),(32,'Tel Aviv-Yafo','Bograshov',8,32.0775921,34.7682231),(33,NULL,NULL,NULL,32.053083,34.7556983),(34,'Tel Aviv-Yafo','Ben Yehuda',94,32.0819414,34.7712213),(35,NULL,NULL,NULL,32.0846551,34.7742076),(36,'Tel Aviv-Yafo','Ahad Ha\'Am',43,32.065584,34.775727),(37,'Tel Aviv-Yafo',NULL,NULL,32.065698,34.7717393),(38,'Tel Aviv-Yafo','Lilienblum',43,32.0625991,34.7730555),(39,'Tel Aviv-Yafo','Maze',3,32.0672674,34.7720585),(40,NULL,NULL,NULL,32.0716167,34.7795405),(41,'Tel Aviv-Yafo','Shlomo ha-Melekh',NULL,32.0763946,34.7766353),(42,'Tel Aviv-Yafo','Har Sinai',5,32.0646762,34.771964),(43,'Tel Aviv-Yafo','King George',30,32.0722304,34.7740944),(44,'Tel Aviv-Yafo','Nahalat Binyamin',29,32.0664912,34.7705135),(45,'Tel Aviv-Yafo','Elifelet',23,32.0577638,34.7640307),(46,NULL,NULL,NULL,32.0640908,34.774046),(47,'Tel Aviv-Yafo','Dizengoff',269,32.0952025,34.7761087),(48,'Tel Aviv-Yafo','Allenby',47,32.070339,34.770221),(49,'Tel Aviv-Yafo','HaShomer',4,32.068496,34.7692798),(50,'Tel Aviv-Yafo','Ibn Gabirol',70,32.0806073,34.7815743),(51,'Tel Aviv-Yafo','Ha-Yarkon',115,32.0813869,34.7681728),(52,'Tel Aviv-Yafo','Rabbi Meir',26,32.0694433,34.7683926),(53,'Tel Aviv-Yafo',NULL,NULL,32.0705236,34.7635345),(54,NULL,NULL,NULL,32.0584547,34.7617025),(55,'Tel Aviv-Yafo','Montefiore',7,32.064974,34.7697759),(56,'Tel Aviv-Yafo','Ahad Ha\'Am',6,32.0631664,34.7683737),(57,'Tel Aviv-Yafo','Sheinkin',33,32.0690179,34.7747451),(58,'Tel Aviv-Yafo','Yigal Alon',96,32.0695301,34.7940875),(59,'Tel Aviv-Yafo',' HaArba\'a',17,32.0707041,34.786478),(60,'Tel Aviv-Yafo','Herzl',146,32.0517915,34.7700436),(61,'Tel Aviv-Yafo',' Yehuda ha-Levi',44,32.061494,34.7727344),(62,'Tel Aviv-Yafo',' Dizengoff',105,32.0798238,34.7737915),(63,'Tel Aviv-Yafo','Levontin',28,32.0630397,34.7766452),(64,'Tel Aviv-Yafo','Montefiore',27,32.0657013,34.7726834),(65,NULL,NULL,NULL,32.0529989,34.7500188),(66,NULL,NULL,NULL,32.0776067,34.78912),(67,'Tel Aviv-Yafo','Beit Eshel',3,32.0545538,34.7558016),(68,'Tel Aviv-Yafo','Sheinkin',56,32.0684685,34.7763989),(69,'Tel Aviv-Yafo','Aluf Kalman Magen',3,32.0713993,34.7865759),(70,'Tel Aviv-Yafo','Weissburg',17,32.1206108,34.828933),(71,'Tel Aviv-Yafo','Ibn Gabirol',88,32.0824886,34.7814816),(72,'Tel Aviv-Yafo','Carlebach',12,32.0700659,34.7827708),(73,'Tel Aviv-Yafo','Laskov',4,32.0712155,34.7824601),(74,'Tel Aviv-Yafo','Frishman',90,32.0793923,34.7798124),(75,NULL,'Khavatselet ha-Sharon',37,32.1789815,34.8046392),(76,'Tel Aviv-Yafo','Yavne',40,32.0629002,34.7741817),(77,'Tel Aviv-Yafo','HaArba\'a',10,32.070217,34.783608),(78,'Tel Aviv-Yafo','Shalom Aleichem',14,32.0760941,34.767826),(79,'Tel Aviv-Yafo','Dizengoff',145,32.0828357,34.7737772),(80,'Tel Aviv-Yafo','Yad Harutsim',13,32.0619565,34.7836617),(81,'Tel Aviv-Yafo',NULL,NULL,32.0542765,34.7775806),(82,'Tel Aviv-Yafo','Yad Harutsim',15,32.0618389,34.7841346),(83,'Tel Aviv-Yafo','Zamenhoff',2,32.0777949,34.7748244),(84,'Tel Aviv-Yafo','Mendele Mokher Sfarim',2,32.0790623,34.768062),(85,'Tel Aviv-Yafo','Retsif Herbert Samuel',90,32.0773932,34.7665794),(86,'Tel Aviv-Yafo','HaArba\'a',14,32.0702291,34.7845926),(87,'Tel Aviv-Yafo','Bograshov',51,32.075923,34.7719574),(88,NULL,'Arieh Shenkar',7,32.1592377,34.8090044),(89,'Tel Aviv-Yafo','King George',81,32.07596,34.776441),(90,'Tel Aviv-Yafo','Ibn Gabirol',14,32.073,34.7820627),(91,NULL,'Ha-Sadna\'ot',10,32.161027,34.806123),(92,'Tel Aviv-Yafo','Ha-Yarkon',205,32.089325,34.770771),(93,'Tel Aviv-Yafo','Ibn Gabirol',123,32.0879518,34.7821173),(94,NULL,'Rachel Imenu',1,31.7630107,35.2184774),(95,NULL,NULL,NULL,32.0530243,34.7720505),(96,NULL,'Ben Yehuda',114,32.0834202,34.7717997),(97,NULL,'Ben Gurion',5,32.1802601,34.872232),(98,NULL,NULL,NULL,32.049975,34.753656),(99,'Tel Aviv-Yafo','Yehuda ha-Levi',52,32.064951,34.77782),(100,'Tel Aviv-Yafo','Dizengoff',276,32.091911,34.776292),(101,'Tel Aviv-Yafo','Allenby',112,32.0640443,34.7725708),(102,'Tel Aviv-Yafo','Yigal Alon',55,32.0627283,34.7919468),(103,'Tel Aviv-Yafo','Kaufmann',6,32.064103,34.762217),(104,'Tel Aviv-Yafo','Chayim Vital',2,32.0569404,34.767795),(105,'Tel Aviv-Yafo','Yigal Alon',98,32.0700804,34.7941446),(106,'Tel Aviv-Yafo','Bograshov',7,32.0777809,34.7683579),(107,'Tel Aviv-Yafo','Ibn Gabirol',8,32.0720644,34.7821624),(108,'Tel Aviv-Yafo',NULL,NULL,32.0658298,34.7767845),(109,NULL,NULL,NULL,32.0781464,34.7891656),(110,'Tel Aviv-Yafo',' Rambam',3,32.0682417,34.7689522),(111,'Tel Aviv-Yafo','Ibn Gabirol',49,32.0769924,34.7811794),(112,'Tel Aviv-Yafo',NULL,NULL,32.0644184,34.7743518),(113,'Tel Aviv-Yafo','Mikveh Israel',26,32.062714,34.7770608),(114,'Tel Aviv-Yafo','Shabazi',10,32.0611268,34.7634915),(115,'Tel Aviv-Yafo',NULL,NULL,32.075354,34.782565),(116,NULL,NULL,NULL,32.066158,34.777819),(117,'Tel Aviv-Yafo','Nahmani',25,32.0659954,34.7750933),(118,'Tel Aviv-Yafo','Berkovitch',4,32.0784362,34.7870601),(119,'Tel Aviv-Yafo','Hillel ha-Zaken',12,32.0702632,34.7695882),(120,'Tel Aviv-Yafo','Dizengoff',275,32.0954014,34.7760846),(121,'Tel Aviv-Yafo','Nahalat Binyamin',80,32.0601078,34.7724625),(122,'Tel Aviv-Yafo','Bat Ami',7,32.0552813,34.7600476),(123,'Tel Aviv-Yafo','Florentin',26,32.0561566,34.7694246),(124,'Tel Aviv-Yafo','Dizengoff',174,32.0849807,34.7746683),(125,'Tel Aviv-Yafo','Shevah',11,32.0616394,34.7835356),(126,'Tel Aviv-Yafo','King George',89,32.0767532,34.7770421),(127,NULL,'Alenby',60,32.0699754,34.7700928),(128,NULL,NULL,NULL,32.0952833,34.7748535),(129,'Tel Aviv-Yafo','Dizengoff',226,32.0888831,34.7755248),(130,NULL,NULL,NULL,32.0674334,34.7618688),(131,NULL,NULL,NULL,32.1006593,34.7751994),(132,'Tel Aviv-Yafo','Dizengoff',98,32.0789293,34.7742042),(133,'Tel Aviv-Yafo','HaTa\'asiya',12,32.0670288,34.7865586),(134,'Tel Aviv-Yafo','Dizengoff',265,32.094667,34.776396),(135,'Tel Aviv-Yafo','Chayim Vital',6,32.0564975,34.7677723),(136,'Tel Aviv-Yafo','Ahad Ha\'Am',54,32.0645393,34.7741587),(137,'Tel Aviv-Yafo','Ha-Yarkon',114,32.0808434,34.7684579),(138,'Tel Aviv-Yafo','Allenby',16,32.0730668,34.7666377),(139,'Tel Aviv-Yafo','Ibn Gabirol',129,32.0886468,34.7822321),(140,NULL,'Ha-Yarkon',98,32.0789691,34.7680004),(141,'Tel Aviv-Yafo',NULL,NULL,32.0534479,34.7538248),(142,NULL,NULL,NULL,32.0709962,34.7883422),(143,'Tel Aviv-Yafo','Ha-Yarkon',66,32.0756509,34.7668682),(144,'Tel Aviv-Yafo','Dizengoff',223,32.0902144,34.7756444),(145,'Tel Aviv-Yafo','Nahalat Binyamin',43,32.0652785,34.7709356),(146,'Tel Aviv-Yafo','Lilienblum',42,32.0623823,34.7721797),(147,'Tel Aviv-Yafo','Mikveh Israel',10,32.0622202,34.7748855),(148,'Tel Aviv-Yafo','Dizengoff',121,32.0811212,34.7737281),(149,'Tel Aviv-Yafo','Ha-Yarkon',102,32.079377,34.7681962),(150,'Tel Aviv-Yafo','Dizengoff',190,32.0856241,34.7748095),(151,'Tel Aviv-Yafo','Ibn Gabirol',13,32.072489,34.781664),(152,'Tel Aviv-Yafo','Brenner',2,32.069141,34.771044),(153,'Tel Aviv-Yafo','Bograshov',18,32.0770918,34.7691322),(154,'Tel Aviv-Yafo','King George',48,32.0743214,34.775838),(155,'Tel Aviv-Yafo',NULL,NULL,32.0870588,34.7691519),(156,'Tel Aviv-Yafo','Abarbanel',13,32.0581096,34.767091),(157,NULL,NULL,NULL,32.0709279,34.7803198),(158,'Tel Aviv-Yafo',' Lilienblum',21,32.0622423,34.7698121),(159,'Tel Aviv-Yafo','Allenby',42,32.0722542,34.768923),(160,'Tel Aviv-Yafo','Allenby',122,32.0628612,34.7730134),(161,'Tel Aviv-Yafo','Chayim Vital',2,32.0569063,34.7677873),(162,'Tel Aviv-Yafo',' Rabi Khanina',8,32.052327,34.755468),(163,'Tel Aviv-Yafo','Levontin',7,32.0617758,34.7747944),(164,'Tel Aviv-Yafo','Dizengoff',117,32.0808107,34.7737328),(165,'Tel Aviv-Yafo',' King George',83,32.0761534,34.7766809),(166,'Tel Aviv-Yafo','Hillel ha-Zaken',8,32.0705137,34.7694419),(167,'Tel Aviv-Yafo','Dizengoff',148,32.0829348,34.7742042),(168,'Tel Aviv-Yafo','Allenby',35,32.0716189,34.7697732),(169,'Tel Aviv-Yafo','Ibn Gabirol',39,32.0761313,34.7813268),(170,NULL,NULL,NULL,32.0630058,34.7719226),(171,'Tel Aviv-Yafo','Allenby',44,32.072036,34.7690678),(172,'Tel Aviv-Yafo','Malkhei Yisra\'el',4,32.0793145,34.7805021),(173,'Tel Aviv-Yafo','Ahad Ha\'Am',54,32.0645535,34.7742794),(174,'Tel Aviv-Yafo','Ben Yehuda',1,32.0732368,34.7680808),(175,NULL,NULL,NULL,32.0780369,34.7736807),(176,'Tel Aviv-Yafo','Yehuda ha-Levi',46,32.0616678,34.7733003),(177,'Tel Aviv-Yafo',NULL,NULL,32.0551164,34.7750196),(178,'Tel Aviv-Yafo','Carlebach',23,32.0682948,34.7828302),(179,'Tel Aviv-Yafo',NULL,NULL,32.0544742,34.7801078),(180,NULL,'Ibn Gabirol',30,32.074968,34.7816739),(181,'Tel Aviv-Yafo',' Nemal Yafo',26,32.0502972,34.7492283),(182,'Tel Aviv-Yafo','Allenby',94,32.0662241,34.7716374),(183,'Tel Aviv-Yafo','King George',48,32.0743404,34.7759128),(184,'Tel Aviv-Yafo','Yigal Alon',126,32.0744509,34.7962091),(185,'Tel Aviv-Yafo','Tversky',6,32.0656672,34.7892622),(186,NULL,NULL,NULL,32.0638447,34.7732667),(187,NULL,NULL,NULL,32.0990312,34.7747085),(188,'Tel Aviv-Yafo',NULL,NULL,32.0628029,34.7695009),(189,'Tel Aviv-Yafo',' HaShah',10,32.0538999,34.7696872),(190,NULL,NULL,NULL,32.0541978,34.7661401),(191,'Tel Aviv-Yafo','Ibn Gabirol',30,32.075067,34.7819048),(192,NULL,NULL,NULL,32.0547107,34.767496),(193,'Tel Aviv-Yafo','Yehuda ha-Levi',43,32.0619841,34.7730318),(194,'Tel Aviv-Yafo','Kaufmann',6,32.0641003,34.7622277),(195,'Tel Aviv-Yafo',NULL,NULL,32.0751486,34.7820792),(196,'Tel Aviv-Yafo','Abarbanel',86,32.0542487,34.7663892),(197,'Tel Aviv-Yafo','HaSharon',21,32.0626748,34.7791932),(198,'Tel Aviv-Yafo','HaShah',12,32.0539868,34.7698438),(199,'Tel Aviv-Yafo','Ibn Gabirol',76,32.0810141,34.7813544),(200,'Tel Aviv-Yafo','Ha-Yarkon',205,32.08917,34.770935),(201,'Tel Aviv-Yafo','Shalom Aleichem',54,32.0785211,34.7708679),(202,'Tel Aviv-Yafo','Eilat',8,32.057182,34.761708),(203,'Tel Aviv-Yafo','Ben Avigdor',15,32.0670678,34.7902374),(204,'Tel Aviv-Yafo',' HaHashmonaim',105,32.0694624,34.7853698),(205,'Tel Aviv-Yafo','Allenby',75,32.0672178,34.7713668),(206,'Tel Aviv-Yafo',NULL,NULL,32.0720839,34.7962723),(207,'Tel Aviv-Yafo','Carlebach',7,32.0668287,34.7832701),(208,'Tel Aviv-Yafo',NULL,NULL,32.1035942,34.8164658),(209,'Tel Aviv-Yafo',NULL,NULL,32.0415502,34.8023265),(210,'Tel Aviv-Yafo','Yigal Alon',126,32.0743997,34.7957343),(211,'Tel Aviv-Yafo','Shadal',7,32.0630814,34.7749041),(212,'Tel Aviv-Yafo','Rambam',14,32.0676891,34.7696633),(213,'Tel Aviv-Yafo','Beit Hilel',7,32.0695376,34.7897598),(214,'Tel Aviv-Yafo','Nahalat Binyamin',43,32.0651828,34.7710124),(215,NULL,'Malkhei Yisra\'el',5,32.0800378,34.7798301),(216,'Tel Aviv-Yafo','Allenby',40,32.0726086,34.7687561),(217,'Tel Aviv-Yafo','Carlebach',3,32.0666333,34.7833329);
/*!40000 ALTER TABLE `Addr` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-17 14:11:31