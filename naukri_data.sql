-- #To create the database
create database edulab;

-- #To use the database
use edulab;

-- #To create the table dataanalyst_ncr
CREATE TABLE `edulab`.`dataanalyst_ncr` (
  `Job_Title` VARCHAR(512) NULL,
  `Experience_Required` VARCHAR(20) NULL,
  `Company_Name` VARCHAR(1024) NULL,
  `Job_Description_Page` VARCHAR(1024) NULL,
  `KeySkills` VARCHAR(1024) NULL,
  `Job_Description` VARCHAR(1024) NULL,
  `Salary` VARCHAR(512) NULL,
  `Job_Id` INT NOT NULL AUTO_INCREMENT,
  `Last_Updated_On` DATETIME NULL,
  PRIMARY KEY (`Job_Id`));


-- #To set the job_id to start from zero
ALTER TABLE dataanalyst_ncr AUTO_INCREMENT=0;

-- #To create the location_jobs table
CREATE TABLE `edulab`.`location_jobs` (
  `Job_Id` INT NOT NULL,
  `Locn_Id` INT NOT NULL,
  `Location` VARCHAR(2048) NULL,
  PRIMARY KEY (`Job_Id`, `Locn_Id`));


-- #To add the foreign key constraint Job_Id
ALTER TABLE `edulab`.`location_jobs` 
ADD CONSTRAINT `Job_Id`
  FOREIGN KEY (`Job_Id`)
  REFERENCES `edulab`.`dataanalyst_ncr` (`Job_Id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

