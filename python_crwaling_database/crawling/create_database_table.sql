-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema shopinfo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shopinfo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shopinfo` DEFAULT CHARACTER SET utf8 ;
USE `shopinfo` ;

-- -----------------------------------------------------
-- Table `shopinfo`.`shop_base_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopinfo`.`shop_base_tbl` (
  `idshop_base_tbl` INT NOT NULL AUTO_INCREMENT,
  `shop_area` VARCHAR(45) NOT NULL,
  `shop_name` VARCHAR(45) NOT NULL,
  `shop_state` VARCHAR(45) NULL,
  `shop_addr` VARCHAR(45) NULL,
  `shop_phone_number` VARCHAR(45) NULL,
  PRIMARY KEY (`idshop_base_tbl`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
