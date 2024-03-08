-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 08, 2024 at 06:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thedailyblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(10) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `message`, `date`) VALUES
(1, 'myname', 'meraemail@gmail.com', '1234567890', 'hello world!', '2024-03-04 13:33:18'),
(2, 'aman', 'am@gmail.com', '56677', 'zbjuhwx', NULL),
(3, 'rahul', 'teraemail@gmail.com', '56217617871', 'hellooooo', '2024-03-04 14:36:59'),
(4, 'aman', 'a@gmail', '2u929i2', '778999', '2024-03-04 22:06:31'),
(5, 'aman', 'a@gmail.com', 'ahha', 'ajajn', '2024-03-04 22:14:11'),
(6, 'aman', 'a@gmail.com', 'ahha', 'ajajn', '2024-03-04 22:15:40'),
(7, 'aman', 'ammyrawat7060@gmail.com', '6288128892', 'hello bhai', '2024-03-04 22:17:31');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(10) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(20) NOT NULL,
  `content` varchar(300) NOT NULL,
  `posted_by` text NOT NULL,
  `posted_on` datetime NOT NULL DEFAULT current_timestamp(),
  `image_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `posted_by`, `posted_on`, `image_name`) VALUES
(1, 'My introduction', 'first post', 'first-post', 'i am a disco dancer', 'Alexis', '2024-03-07 12:12:10', 'post-bg.jpg'),
(2, 'Github', 'explanation about github', 'second-post', 'GitHub (/ˈɡɪthʌb/[a]) is a developer platform that allows developers to create, store, manage and share their code. It uses Git software, providing the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration. ', 'aman', '2024-03-05 23:24:04', ''),
(3, 'Google ', 'google ka intro', 'third-post', 'Google LLC (/ˈɡuːɡəl/ ⓘ, GOO-ghəl) is an American multinational corporation and technology company focusing on online advertising, search engine technology, cloud computing, computer software, quantum computing, e-commerce, consumer electronics, and artificial intelligence (AI).[9] It has been refer', 'sunny', '2024-03-05 23:48:09', ''),
(4, 'Cricket ki news', 'junnon', 'fourth-post', 'Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps.', 'tushar', '2024-03-05 23:49:27', ''),
(5, 'Facebook, Instagram down globally, users complain of being logged out', 'tagdi news\r\n', 'fifth-post', 'Downdetector, a website that tracks outages, has recorded over 3,00,000 Facebook outages and over 47,000 outage reports for Instagram worldwide.', 'mark', '2024-03-05 23:50:19', ''),
(7, 'Python', 'Easy language', 'seventh-post', 'Language easy to understand and learn. Easy to understand syntax.', 'coder', '2024-03-07 12:37:57', 'img.png'),
(8, 'Python', 'Easy language', 'seventh-post', 'Language easy to understand and learn.', 'coder', '2024-03-07 11:18:04', 'img.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`),
  ADD KEY `slug` (`slug`),
  ADD KEY `slug_2` (`slug`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
