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
-- Table structure for table `Clubs`
--

DROP TABLE IF EXISTS `Clubs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clubs` (
  `idClubs` int(11) NOT NULL AUTO_INCREMENT,
  `addr_id` int(11) DEFAULT NULL,
  `name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `googleId` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`idClubs`),
  UNIQUE KEY `idNightClubs_UNIQUE` (`idClubs`),
  UNIQUE KEY `googleId_UNIQUE` (`googleId`),
  KEY `addr_id_club_idx` (`addr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clubs`
--

LOCK TABLES `Clubs` WRITE;
/*!40000 ALTER TABLE `Clubs` DISABLE KEYS */;
INSERT INTO `Clubs` VALUES (1,130,'Clara Club',3.3,'4596e8a5fac1bd0f894500fa84400620d3dc5a7e'),(2,141,'Anna Loulou Bar',4.3,'b6d039c6d8c3ba39337d3ba2268e01367174ba79'),(3,147,'KULI ALMA',4.3,'4d58f4345fb1f8ca943c76d8376643a797e0e799'),(4,170,'JIMMYWHO? Bar & Lounge',3.9,'414ce402d31ebcedebb28b637643b196980f6ffc'),(5,173,'Alphabet',4.2,'b703297d43658f4bd429088274d294c00d0be823'),(6,174,'Langa Club',3.8,'67df1a11c093a095f96c1140941182fb9bd7737f'),(7,175,'dizingoff club',NULL,'dc74d9ec631b4cd9dc53a100fcab099e6ca56475'),(8,176,'Solo Club Tel Aviv',3.6,'a81c4bbde00e140ebcef8c0788839c1ca9976f75'),(9,177,'Ku Club Tel Aviv',4.2,'6e42468c5f6b39768a90a04f820d78395659df1f'),(10,178,'The Cat & Dog',3.6,'72841b2ccbc75b77e3d1e6a9d5098020a3cdbef7'),(11,179,'The Block',4.4,'1ad62d420b8a37da0ff08d759e89c2d245564aa0'),(12,180,'Markid Tel Aviv | ×ž×¨×§×™×“',NULL,'bc688e1cd610de76c91b63408db520c9a1b07d99'),(13,181,'TLV Club',NULL,'b62c0b55d70a55c0c87be864317fe13833865c1f'),(14,182,'Pasaz',4.5,'e53f4478f4c770eebae9cbe6f277c98cb3197c1f'),(15,183,'Bootleg',4.1,'f07aa48f5982cb9dc5c14b69b3120df3e9b016e2'),(16,184,'Havana Music Club',4.1,'fa738a9cf85ccc386d1a968670f8bcfacb930bc7'),(17,185,'×ž×•×¢×“×•×Ÿ ×—×©×¤× ×•×ª - Bursa Club',3.3,'49a5093b1c029fdf46b62b28196be691d14d7c5a'),(18,186,'BuXa',4.3,'585ee6e56a65975dba7ef20bf99eeafbe01ee125'),(19,187,'Shablul Jazz Club',3.9,'214dfd1f94a119d97a1e044294fc99222e00a65d'),(20,188,'The Breakfast Club',4,'9bfb5b760a3bfb03e52a08afb84fc374258396df'),(21,189,'Duplex',4.3,'ca0d52381b64304e84cb8366a63836bb12bdeba8'),(22,190,'Haoman 17',3.8,'d18f8808e8edad33576eb39e04194c94b6dfe5b2'),(23,191,'Dream Exhibition Club',NULL,'e69650a44bd57e18293b8433309dec69f3e341b1'),(24,192,'Gagarin Club TLV',4.2,'0a25496ed8c56607ba7324bae779e46c2726b82f'),(25,193,'Penguin Club',NULL,'56cba5c5754bbfc0fa54ffdc7f6340a337f4e4bd'),(26,194,'Sublet Bar',NULL,'6e498d41b39d5834ce9e06bcaeb5ace423c0445b'),(27,195,'Morfuim Forte',3.4,'95ebc4feae5a44ca1094800d8082edf2bf0420dc'),(28,196,'Baby Dolls',3.4,'438fe76448ff6c46eb6d1343062290d017d373ff'),(29,197,'×”×“×× ×’\'×Ÿ',4.3,'e25effcd00b34acf3610e305d2b3323b6a8b2482'),(30,198,'hamosad club - ×ž×•×¢×“×•×Ÿ ×”×ž×•×¡×“',3.7,'4ee874860fbedf4756606c8711699429de5a9a90'),(31,199,'Panda club',NULL,'da30029d1212c40dcc46e5129e4cb92e9cfe136d'),(32,200,'Hilton Tel Aviv',4.1,'c4013adba4a86c307737bc41d25050fbb18abae8'),(33,201,'TLV VIP Nightlife',NULL,'1f6f362e47a1af082ede329f9450d5bc40263907'),(34,125,'Bar 911',4.6,'ddd4391c2042e8a2aa57b522889584c63275d3d2'),(35,202,'Shmone',NULL,'22c472b58847bb40b3c58c2e7220eecf55e46a54'),(36,203,'LEO Club Tel Aviv',NULL,'321331aa7a97f174914b3260577e1f1fb49d83d2'),(37,204,'Tel Aviv',NULL,'08d2b1ad4ba06749fb20997f531f212e667916ef'),(38,205,'Sauna Paradise',3.2,'f3342bd942a31b5ef6832474a10032c6fb02ceae'),(39,206,'×“×™×¤×¨× ×˜ ×œ×•×¤×˜ ×œ××™×¨×•×¢×™×',NULL,'d4384fc1dc3c2b463510bf3de60a3e120a4ba9a9'),(40,207,'×–×™×–×™ ×˜×¨×™×¤×•',NULL,'739aa9e9669b0bfecb7badf538356ac14b2bc2b6'),(41,208,'Seating Dawn',NULL,'e6113f8a1be1bf190fb0b93c2ea97a9813d3a1b4'),(42,209,'Ð¡ÑƒÑ‡Ð¸Ð¹ ÐŸÐ°Ñ€Ðº',NULL,'5f820062c7b1c162176d4c04338e4412fce98140'),(43,210,'××œ×ž×” ×“×” ×§×•×‘×”',4.5,'d888852889c9530cf7dd63f8ea8216cfba2f39cb'),(44,211,'Club Radio',NULL,'2a38705b953f6bcb25637d8ea29f286715e366f0'),(45,212,'×‘×™×ª ×”×¢×ž×•×“×™×',4.3,'9055021b072f2820c6523c8c922590901c17fce8'),(46,213,'Cyber Quest Israel',4.3,'3a8c7603500e0dbc79533bffb961ee66bce6a909'),(47,215,'Malki',4.2,'d7b9829ddfceef930f35ffe7f6eafce881a9e214'),(48,216,'40 Alenbi',3.7,'cc30b651498742b5036842df74ed0769bcd5764f'),(49,217,'Jelsomino and Friends',3.9,'c50b7cb09633152e513d00d246c94461ccaf7f0d');
/*!40000 ALTER TABLE `Clubs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-17 14:11:37
