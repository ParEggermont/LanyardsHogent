CREATE TABLE `gaat_naar` (
  `student_id` int NOT NULL,
  `les_id` int NOT NULL,
  `gaat_naar` tinyint DEFAULT NULL,
  PRIMARY KEY (`student_id`,`les_id`),
  KEY `les_idx` (`les_id`),
  CONSTRAINT `les` FOREIGN KEY (`les_id`) REFERENCES `les` (`les_id`),
  CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB