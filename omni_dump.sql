-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: omni
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

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
-- Table structure for table `actor`
--

DROP TABLE IF EXISTS `actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor` (
  `id` varchar(60) NOT NULL,
  `added_at` datetime DEFAULT NULL,
  `last_name` varchar(32) NOT NULL,
  `first_name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor`
--

LOCK TABLES `actor` WRITE;
/*!40000 ALTER TABLE `actor` DISABLE KEYS */;
INSERT INTO `actor` VALUES ('0388d241-e53a-4cf1-81a4-53b47dd09b85','2022-11-23 00:00:00','Audu','Judith'),('73392748-c49d-4699-bb64-fb70b2253730','2022-11-23 00:00:00','Onyeka','Mercy'),('7cc8799c-0625-48e4-9263-8fb34b2546f8','2022-11-23 00:00:00','Annan','Toosweet'),('a88b944e-9ea3-4670-b02a-46eb41f3483a','2022-11-23 00:00:00','Effiong','Daniel'),('ac9cf978-1445-438d-843e-3c21de27d293','2022-11-23 00:00:00','Anthony','Racheal'),('b28263c6-a7de-47d3-8ec9-5991b822b6c1','2022-11-23 00:00:00','Maurice','Sam'),('bfbc61d2-beb8-4083-94db-707287e3a0e2','2022-11-23 00:00:00','Kadiri','Ruth'),('d086e50e-052f-4324-992f-733af46f3fe3','2022-11-23 00:00:00','Rosman','Shine'),('efe103a7-35b4-4897-92f6-ee51c23ccc8b','2022-11-23 00:00:00','Nwadike','Kenneth');
/*!40000 ALTER TABLE `actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `id` varchar(60) NOT NULL,
  `added_at` datetime DEFAULT NULL,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES ('43cb9232-52c6-4e6c-9c84-48c776d1f0f5','2022-11-21 00:00:00','Romance'),('ded6288a-6e3f-4809-8318-f7d0bae223bc','2022-11-23 00:00:00','Drama');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `id` varchar(60) NOT NULL,
  `added_at` datetime DEFAULT NULL,
  `url` varchar(64) NOT NULL,
  `title` varchar(32) NOT NULL,
  `series` tinyint(1) DEFAULT NULL,
  `rated_18` tinyint(1) DEFAULT NULL,
  `genre_id` varchar(64) NOT NULL,
  `thumbnail` varchar(64) DEFAULT NULL,
  `description` varchar(2096) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES ('0864f73b-f116-4735-a3ed-7152d2686770','2022-11-23 00:00:00','https://www.youtube.com/embed/9dK-HC8t_yI','Unintentional',0,0,'ded6288a-6e3f-4809-8318-f7d0bae223bc','https://img.youtube.com/vi/9dK-HC8t_yI/maxresdefault.jpg','They say love hits when you least expect it. What if you unexpectedly create it, then you blow it and now you have to figure out how you lost it! Unintentional follows Sefi Madaki on an adventure that leads everywhere but where she planned. It is a story of self-discovery and the power of fate. Follow this romantic comedy to laugh, dream and root for love this season'),('45e34000-194f-4fd5-922d-c6306ec87f0f','2022-11-23 00:00:00','https://www.youtube.com/embed/p7cnVRqug8c','Best Friends Forever',0,0,'ded6288a-6e3f-4809-8318-f7d0bae223bc','https://img.youtube.com/vi/p7cnVRqug8c/maxresdefault.jpg','When Laura introduces her fiance to her best friend Evie. However, Evie and Dave had a history together. What will this mean for their relationship'),('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','2022-11-21 00:00:00','https://www.youtube.com/embed/wr0QR8rznAA','Lets switch wives',0,0,'43cb9232-52c6-4e6c-9c84-48c776d1f0f5','https://img.youtube.com/vi/wr0QR8rznAA/maxresdefault.jpg','Couples set to divorce their partners in court, must meet one last court order before their divorce is finalized'),('bd846631-7f85-4a77-9761-8b85d9a7599a','2022-11-23 00:00:00','https://www.youtube.com/embed/MyVG-UcdLU8','The perfect assitant',0,0,'43cb9232-52c6-4e6c-9c84-48c776d1f0f5','https://img.youtube.com/vi/MyVG-UcdLU8/maxresdefault.jpg','A man finds it difficult to carter for himself, until an oppurtunity landed at his feet. Just one jobwill make a differenecin his life'),('d6e600c8-12e0-4d96-9725-a5ebf7b85d84','2022-11-23 00:00:00','https://www.youtube.com/embed/U64A2f4O6KE','Victorias Secret',0,0,'ded6288a-6e3f-4809-8318-f7d0bae223bc','https://img.youtube.com/vi/U64A2f4O6KE/maxresdefault.jpg','Burdened with her mothers debt and the loss of a sister, victoria goes on a journey to conquer her fears and challanges, What does live have in store for her?');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_actors`
--

DROP TABLE IF EXISTS `movie_actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_actors` (
  `movie_id` varchar(60) DEFAULT NULL,
  `actor_id` varchar(60) DEFAULT NULL,
  KEY `movie_id` (`movie_id`),
  KEY `actor_id` (`actor_id`),
  CONSTRAINT `movie_actors_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `movie_actors_ibfk_2` FOREIGN KEY (`actor_id`) REFERENCES `actor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_actors`
--

LOCK TABLES `movie_actors` WRITE;
/*!40000 ALTER TABLE `movie_actors` DISABLE KEYS */;
INSERT INTO `movie_actors` VALUES ('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','0388d241-e53a-4cf1-81a4-53b47dd09b85'),('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','73392748-c49d-4699-bb64-fb70b2253730'),('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','bfbc61d2-beb8-4083-94db-707287e3a0e2'),('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','7cc8799c-0625-48e4-9263-8fb34b2546f8'),('9a4de33a-ad02-4ebf-b4cb-b75b3c4e38b9','efe103a7-35b4-4897-92f6-ee51c23ccc8b');
/*!40000 ALTER TABLE `movie_actors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-01 21:18:30
