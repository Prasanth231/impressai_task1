-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2023 at 06:32 AM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `impressai`
--

-- --------------------------------------------------------

--
-- Table structure for table `ai`
--

CREATE TABLE IF NOT EXISTS `ai` (
  `TOTAL` int(11) DEFAULT NULL,
  `STUPID` int(11) DEFAULT NULL,
  `FAT` int(11) DEFAULT NULL,
  `DUMP` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ai`
--

INSERT INTO `ai` (`TOTAL`, `STUPID`, `FAT`, `DUMP`) VALUES
(77, 37, 16, 23);

-- --------------------------------------------------------

--
-- Table structure for table `impress`
--

CREATE TABLE IF NOT EXISTS `impress` (
  `id` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `stupid` int(11) NOT NULL,
  `fat` int(11) NOT NULL,
  `dumb` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `impress`
--

INSERT INTO `impress` (`id`, `user`, `stupid`, `fat`, `dumb`) VALUES
('851841321', 'haha198', 2, 3, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
