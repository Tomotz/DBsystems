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
-- Table structure for table `Bars`
--

DROP TABLE IF EXISTS `Bars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bars` (
  `idBar` int(11) NOT NULL AUTO_INCREMENT,
  `addr_id` int(11) DEFAULT NULL,
  `name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `googleId` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`idBar`),
  UNIQUE KEY `idBar_UNIQUE` (`idBar`),
  UNIQUE KEY `googleId_UNIQUE` (`googleId`),
  KEY `addr_id_idx` (`addr_id`),
  CONSTRAINT `addr_id_bar` FOREIGN KEY (`addr_id`) REFERENCES `Addr` (`idAddr`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bars`
--

LOCK TABLES `Bars` WRITE;
/*!40000 ALTER TABLE `Bars` DISABLE KEYS */;
INSERT INTO `Bars` VALUES (1,33,'Onza',4.2,'c4586e958c2899b278a7553ca5503c4c068f43fb'),(2,37,'Zakaim',4.1,'68fb5164aabd7f74ee5bfc867aca967278adce47'),(3,44,'Bicicletta',4.3,'3ea3914a67fbcff986a5f6f1b092d3bda0111917'),(4,126,'Silon',4.4,'1d0d244ac882d676105deffbbf57d6765b7b9a1a'),(5,127,'HaMinzar',4.5,'df168039405b000d6efef45a4293ab228e0da4a7'),(6,128,'Rubi',4.1,'2a24c84bf5b97dc5771b8f33c42167d0d1e97d53'),(7,129,'Mate - ×“×™×–×™× ×’×•×£',4.2,'62d32be4c573b7de944160263ef9a153d6251f52'),(8,130,'Clara Club',3.3,'4596e8a5fac1bd0f894500fa84400620d3dc5a7e'),(9,131,'Litzman Bar - ×œ×™×¦×ž×Ÿ ×‘×¨',4,'fe44038d91125a9ecc5e8e67fa3a30660764b524'),(10,132,'Ismi Salma',3.8,'d481f2173a680b5454f685f52ed3a6e12820a3f0'),(11,45,'Norma Jean',4.4,'f63ae2aa4d438f880d397e62e23202c8e187a6e1'),(12,133,'The Dancing Camel Brewery',4.3,'23e7d86cc02bdcd2234491ebf1fba46a8fe4e031'),(13,134,'Rosa Parks',4.5,'feb257fb577834b37bebcdf985153132f4485924'),(14,135,'Jackson Bar',4.2,'d01e0b48193af403f01924f5e289295950fce0d7'),(15,136,'OTTO',3.5,'96bc6d464d595302063ef2c465ae1716862252e9'),(16,137,'Patio bar - Patio Bar',3.9,'ddda235ae665d4b6ef5b72d5633805afd64135a3'),(17,138,'Potion Bar',4.1,'778a39c88336bca07bcf1adb7a0e3e47c60b24e7'),(18,139,'Agnes Tel Aviv',4,'d30890a9391077c525a93d76680bc4109c2dd173'),(19,140,'Mash Embassy',NULL,'b22620530633532c5f22ac2f6fc0d14b1ae31376'),(20,141,'Anna Loulou Bar',4.3,'b6d039c6d8c3ba39337d3ba2268e01367174ba79'),(21,142,'Jajo Wine Bar',3.8,'028d06d6978c7edb6a38a5db55300217ed9a9936'),(22,46,'Patrick\'s',3.8,'5246d2815138b27d47374ff3e2be92887bbb0dfb'),(23,49,'HaBasta',4.1,'7c62186251b9e8460f40d7ed41ddf9ce2fef7177'),(24,53,'Banana Beach',3.9,'a820858876d79ba4a684bf0be73dd60607f4a2af'),(25,54,'Vicky Cristina',4.1,'4a7d23ed7c22dffdfac204f05dc894204c0f9634'),(26,66,'Meatos',3.7,'b8ee373ab0b5f3b16cffce863f3406345f8f0ee2'),(27,143,'Imperial Cocktail Bar',4.5,'6f9a17b5bc2579676a393cad6ab1ec38152b59ab'),(28,144,'223',4.1,'3ad8045bc0ae1b376e36e1d64535ef399e373417'),(29,145,'Shpagat',4.3,'c86ace7c6977fa85328b74395e5e779bedea506f'),(30,84,'Molly Bloom\'s',4.4,'e0aa6a8c8c7ae90e717f7cc5dc59cc827dc17aa5'),(31,146,'Lima Lima bar',4.1,'d92cb1bb428efccd52182641cb2b11fec8251745'),(32,147,'KULI ALMA',4.3,'4d58f4345fb1f8ca943c76d8376643a797e0e799'),(33,148,'Dizzy Frishdon',3.9,'1174e411d4e795e19e5b703ea876a7c792667d12'),(34,149,'Mendalimos',3.8,'d199d65a2f8456466459d433609a4f4e7c7a53a7'),(35,150,'Jasper Johns Bar',4.5,'a8a91783f27f077fa20afe854aea5cd56ee622a8'),(36,151,'Backy Bar',4.4,'b68376c9d6959cc95950a60af1445c1718a1367d'),(37,152,'French 57',4.7,'4c4ae4fcb0d4c90d0af1b7915825781c424f3993'),(38,153,'Biggy Z',4.2,'2797734a1d568883c86a74d0860423edd4fee986'),(39,154,'Ozen Bar',4.1,'df4fe4ba02983e12c423dd3c23c3745a2e54117a'),(40,155,'Esperanto - Drinks & Summer Bites',4.1,'d001ad8af1b2c18025f5c5f84c4669162f4d6c69'),(41,156,'Hoodna',4.3,'dbc6bf7ae780cc87f0810a9e35637a39c599c445'),(42,85,'Mike\'s Place',4.1,'7f1129f3fccc53e031fa7b082645b7ff3a05ffb0'),(43,157,'Bellboy',4.6,'fe92a0635dd17c196c457bc4e3487a123d6e9ac1'),(44,158,'Cofix Bar',4.5,'81ce5fdc275bdb3924f49689a3cf91bc6ed1120c'),(45,86,'Mike\'s Place',3.8,'485ad489fb7daea2192fefb276365893e1dce22a'),(46,159,'Joey\'s bar',4.2,'22c37715f2a5638c7f27518874c5ce366eec4997'),(47,112,'Social Club',3.9,'5a5c2ac34c5b27311e4db965d1ae1519fe1e8328'),(48,160,'Sputnik Bar',4.2,'75a0c664c5bfba7265893af8c4b9b308ed3c094a'),(49,161,'Satchmo',4.5,'53800e3440404298148778df0f2ce4123abdfbf2'),(50,122,'Par Derriere',4.3,'11cb0505f2e0ef097bb29af682fcc9e974e624d3'),(51,162,'Passpartu',4.4,'61177a44fbdac4e70ee32ba0f637d181d602f18e'),(52,163,'Levontin 7',4.2,'8c3b103c5d2a9f4200ad0425e333f8880fef347d'),(53,164,'×¡×¤×™×™×¡ ×”××•×¡',4.3,'a56b525d156c66a596d6d99e6208b54b8a491622'),(54,165,'Denim Drinks First',4.2,'c5f40931b9e369291c1784b10c16fc15f3e7c750'),(55,166,'× ×•×¨×ž×Ÿ ×‘×¨',4.7,'4d6dae6048bc302420467fc61859c040839fa487'),(56,167,'Ilka',3.8,'627cdf890ba814c81360f91d7bb904ce8e456d35'),(57,168,'Temptation',4.2,'2e6a7d9332e38aff66f7cbf10f756f50e903af4c'),(58,169,'HaShoftim Pub',4.4,'545238b72e7c47f5243c005eb3d1271fa269fb2f'),(59,123,'Bugsy',4.1,'6fa6a6c3b72afeb642a31a3d03cd0b89a32939df'),(60,170,'JIMMYWHO? Bar & Lounge',3.9,'414ce402d31ebcedebb28b637643b196980f6ffc'),(61,124,'Cerveza',4.2,'ae1c1e210a78319765b5071fac4dbb23becb0e6c'),(62,171,'Chaser',3.5,'0297b437069395a6b509933890aa049e81579fb7'),(63,172,'Louis',3.9,'8c6187ff852df10aa8d78e0bff39d1516b1f4fa7'),(64,173,'Alphabet',4.2,'b703297d43658f4bd429088274d294c00d0be823'),(65,175,'dizingoff club',NULL,'dc74d9ec631b4cd9dc53a100fcab099e6ca56475'),(66,185,'×ž×•×¢×“×•×Ÿ ×—×©×¤× ×•×ª - Bursa Club',3.3,'49a5093b1c029fdf46b62b28196be691d14d7c5a'),(67,186,'BuXa',4.3,'585ee6e56a65975dba7ef20bf99eeafbe01ee125'),(68,187,'Shablul Jazz Club',3.9,'214dfd1f94a119d97a1e044294fc99222e00a65d'),(69,188,'The Breakfast Club',4,'9bfb5b760a3bfb03e52a08afb84fc374258396df'),(70,200,'Hilton Tel Aviv',4.1,'c4013adba4a86c307737bc41d25050fbb18abae8'),(71,125,'Bar 911',4.6,'ddd4391c2042e8a2aa57b522889584c63275d3d2'),(72,205,'Sauna Paradise',3.2,'f3342bd942a31b5ef6832474a10032c6fb02ceae'),(73,212,'×‘×™×ª ×”×¢×ž×•×“×™×',4.3,'9055021b072f2820c6523c8c922590901c17fce8'),(74,213,'Cyber Quest Israel',4.3,'3a8c7603500e0dbc79533bffb961ee66bce6a909'),(75,214,'Mini Club',NULL,'70e5bfd4bd24a00e9888b168c79b7cefda2944a4'),(76,217,'Jelsomino and Friends',3.9,'c50b7cb09633152e513d00d246c94461ccaf7f0d');
/*!40000 ALTER TABLE `Bars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-17 14:11:29
