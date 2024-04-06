-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: discussion_board
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `username` varchar(10) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('nagu','nagalakshmijarugulla2003@gmail.com','hello1');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `postid` int DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `comment` text,
  `date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cid`),
  KEY `postid` (`postid`),
  KEY `email` (`email`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`postid`) REFERENCES `post` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`email`) REFERENCES `users` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (27,4,'nagalakshmijarugulla2003@gmail.com','nice','2023-07-05 13:15:10'),(28,4,'nagalakshmijarugulla2003@gmail.com','nice','2023-07-05 13:17:54'),(29,4,'nagalakshmijarugulla2003@gmail.com','hi','2023-07-05 17:05:50'),(30,4,'nagalakshmijarugulla2003@gmail.com','how are you','2023-07-05 17:11:01'),(31,4,'nagalakshmijarugulla2003@gmail.com','what are you doing','2023-07-05 17:15:32'),(32,5,'nagalakshmijarugulla2003@gmail.com','hi','2023-07-05 17:17:11'),(33,5,'nagalakshmijarugulla2003@gmail.com','em chestunav','2023-07-05 17:17:52'),(34,5,'nagalakshmijarugulla2003@gmail.com','ra bayatiki veldham ','2023-07-05 17:24:00'),(35,4,'nagalakshmijarugulla2003@gmail.com','how are you','2023-07-05 17:30:47'),(36,4,'nagalakshmijarugulla2003@gmail.com','job yanti','2023-07-05 17:38:45'),(37,4,'nagalakshmijarugulla2003@gmail.com','hi','2023-07-05 17:40:19'),(38,4,'nagalakshmijarugulla2003@gmail.com','','2023-07-05 17:41:38'),(39,4,'nagalakshmijarugulla2003@gmail.com','poiu','2023-07-05 17:52:17'),(40,7,'nagalakshmijarugulla2003@gmail.com','nice','2023-07-05 17:59:42'),(41,7,'nagalakshmijarugulla2003@gmail.com','who r u','2023-07-05 18:00:37'),(42,7,'nagalakshmijarugulla2003@gmail.com','fine','2023-07-05 18:08:32'),(43,7,'nagalakshmijarugulla2003@gmail.com','chyjdbnxbj','2023-07-05 18:09:42');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `title` varchar(30) DEFAULT NULL,
  `content` text,
  `date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`pid`),
  KEY `email` (`email`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`email`) REFERENCES `users` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (4,'nagalakshmijarugulla2003@gmail.com','hello','dsifasjkbdjfb','2023-06-24 17:08:16'),(5,'nagalakshmijarugulla2003@gmail.com','mn,n','m n,n','2023-06-24 16:30:45'),(7,'nagalakshmijarugulla2003@gmail.com','ME,MYSELF AND I','always know your self more than others self\r\nbelief your self','2023-07-05 17:57:24');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reply`
--

DROP TABLE IF EXISTS `reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reply` (
  `reply` text,
  `cid` int DEFAULT NULL,
  KEY `cid` (`cid`),
  CONSTRAINT `reply_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `comments` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reply`
--

LOCK TABLES `reply` WRITE;
/*!40000 ALTER TABLE `reply` DISABLE KEYS */;
INSERT INTO `reply` VALUES ('hello',27),('iam good',27),('how are yoyu',27),('hiii',30),('iam good',30),('iam a coder',31),('hi how are you',32),('em ledu kali',33),('yandhuku yakkadiki',34),('iam good',27),('kaliha untuna',27),('hello',27),('',27),('asdf',27),('hiusahcugds',39),('yeah',40),('me too',40),('svgvcg',43),('gsvtybvy',43),('fyhcy',43);
/*!40000 ALTER TABLE `reply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(20) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('nagalakshmi','nagalakshmijarugulla2003@gmail.com','hi');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-05 20:22:53
