CREATE SCHEMA Project;
USE Project;

CREATE TABLE Signup (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    UserName VARCHAR(255) UNIQUE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE `user_profile` (
  `UserID` int NOT NULL,
  `FullName` varchar(255) NOT NULL,
  `Age` int NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Location` varchar(255) NOT NULL,
  `SportsInterest` varchar(255) NOT NULL,
  `SkillLevel` varchar(45) NOT NULL,
  `Availability` varchar(45) NOT NULL,
  PRIMARY KEY (`UserID`),
  CONSTRAINT `UserID` FOREIGN KEY (`UserID`) REFERENCES `signup` (`ID`)
)

