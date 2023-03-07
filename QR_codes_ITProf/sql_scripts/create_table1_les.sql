CREATE TABLE `les` (
  `naam` varchar(70) NOT NULL,
  `tijdslot` varchar(45) NOT NULL,
  `spreker` varchar(45) NOT NULL,
  `locatie` varchar(45) NOT NULL,
  `dag` varchar(45) NOT NULL,
  `les_id` int NOT NULL,
  PRIMARY KEY (`les_id`)
) ENGINE=InnoDB 