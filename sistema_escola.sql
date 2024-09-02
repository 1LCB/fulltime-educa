-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 15/06/2024 às 19:32
-- Versão do servidor: 10.4.24-MariaDB
-- Versão do PHP: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sistema_escola`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `classes`
--

CREATE TABLE `classes` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `status` enum('active','inactive','other_option') DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `evaluations`
--

CREATE TABLE `evaluations` (
  `id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `sector_id` int(11) DEFAULT NULL,
  `total_classes` int(11) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  `absences` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `groups`
--

INSERT INTO `groups` (`id`, `name`) VALUES
(1, 'Alunos'),
(2, 'teachers');

-- --------------------------------------------------------

--
-- Estrutura para tabela `group_permissions`
--

CREATE TABLE `group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `schools`
--

CREATE TABLE `schools` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `schools`
--

INSERT INTO `schools` (`id`, `name`) VALUES
(1, 'Escola1\r\n');

-- --------------------------------------------------------

--
-- Estrutura para tabela `sectors`
--

CREATE TABLE `sectors` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `sectors`
--

INSERT INTO `sectors` (`id`, `name`) VALUES
(1, 'Setor1');

-- --------------------------------------------------------

--
-- Estrutura para tabela `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` enum('male','female','other') DEFAULT NULL,
  `ethnicity` varchar(50) DEFAULT NULL,
  `birth_city` varchar(100) DEFAULT NULL,
  `id_card` varchar(20) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `residential_complement` varchar(255) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `mother_name` varchar(100) DEFAULT NULL,
  `school_attended` int(11) DEFAULT NULL,
  `current_school` int(11) DEFAULT NULL,
  `shift` varchar(50) DEFAULT NULL,
  `sector_id` int(11) DEFAULT NULL,
  `admission_date` date DEFAULT NULL,
  `completion_date` date DEFAULT NULL,
  `course_status` varchar(50) DEFAULT NULL,
  `total_classes` int(11) DEFAULT NULL,
  `attendances` int(11) DEFAULT NULL,
  `absences` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `students`
--

INSERT INTO `students` (`id`, `user_id`, `date_of_birth`, `gender`, `ethnicity`, `birth_city`, `id_card`, `cpf`, `phone`, `address`, `residential_complement`, `father_name`, `mother_name`, `school_attended`, `current_school`, `shift`, `sector_id`, `admission_date`, `completion_date`, `course_status`, `total_classes`, `attendances`, `absences`) VALUES
(1, 1, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(2, 2, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(3, 3, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(4, 4, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(5, 5, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(6, 6, '0000-00-00', '', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(7, 7, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(8, 8, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(9, 9, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(10, 10, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(11, 11, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(12, 12, '0000-00-00', '', 'aaaaaaaa', '2024-06-16', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaa', 'aaaaaa', 1, 1, 'manha', 1, '2024-06-16', '2024-06-18', 'aaaaaaaa@email.com', 0, 0, 0),
(13, 13, '0000-00-00', '', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 'aaaaaaaa@em', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 'aaaaaaaa@email.com', 1, 1, 'tarde', 1, '2024-06-26', '2024-06-11', 'aaaaaaaa@email.com', 0, 0, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `students_classes`
--

CREATE TABLE `students_classes` (
  `id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `teachers`
--

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `group_id`, `image_path`) VALUES
(1, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$iVh7TPWnIqPK9NTQhDyLL.eRZ9xoNLJ0Xz44VoeEAJoO/Sou0uAZu', 1, '51543a4f-4d73-4915-997d-997903e5c41a.jpg'),
(2, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$ciGeShfT./HoDyHzJbixYOC10ErkVIaCYWaGIMg4j.SCOrmLKKGZC', 1, '56132c34-9463-4b8e-9b97-0b38a30ebec2.jpg'),
(3, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$4vk7tSJnSSlOdZ7EYos3VOlP.5sA916xTpuhvkTDhiTXD5p.LAQBq', 1, 'da086106-4267-4b77-9189-f377e096e572.jpg'),
(4, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$rao/32L8btQW0Fmsc4w.cuuV3Qwpska/pGRIm1R6lReF7tTrvV76S', 1, '7283c6e6-4903-4034-82b8-7dafad1b2361.jpg'),
(5, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$v3KI/T/dU/oV45bfUKWeSuYR1Jyl4c1H9POlEdaFOlFyUdET0qmcC', 1, '50753547-22d3-41da-9c0a-f0f1b64e3539.jpg'),
(6, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$WfXM6.4TGd2vkFstfzZu7uw2L.vZjqzEft5EeQVdG856f7Irn.n76', 1, '243d5865-02a1-46b3-942d-ab2b356f19ee.jpg'),
(7, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$xHr0870C0XyEoTjUlYttgeRFDM0XCr0cq6xGS0BFlk0FoEbCYM60.', 1, 'c3658975-63fa-4baa-bdec-61c1c03bd09e.jpg'),
(8, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$iNtK.FECSm7m.caYaD5CVOhVqcu.bBx4H9NyYbbdudR/B..kPfmUu', 1, '30889141-e503-4ed6-bcbb-467244a05f8d.jpg'),
(9, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$BdmvcfVF0TDpUyvHkWuB5.JtF277yx5dvIstUvZyLVvA2N/VVAEF6', 1, '2abc3b71-d940-4483-803c-01113d2501b0.jpg'),
(10, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$Gg.nobDSIaPJWJOfFd3A3.vkZo/l2MKIdviCU68UH5WR6MJgv.Il2', 1, '8cc2eb23-572a-445c-ad06-ab8b23bf9b7c.jpg'),
(11, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$ueLs86/5N4I5W1g4tV4Ymu8IvEbREDgrqGlwwCPLQpNfsR9W828km', 1, 'f791fcea-2491-4696-a847-078f392c044b.jpg'),
(12, 'aaaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$VP7KDN1KEt019qe5IT/h6uaXXsHcSu5rTavIW6a8qZtchFFCdaloO', 1, 'a1e758f1-042e-4daf-a997-7009fb9d9258.jpg'),
(13, 'aaaaaaaaa', 'aaaaaaaa@email.com', '$2b$15$SW79XKbKv467NU8r0C3bJuuPJGyUa8mwq6E/GwWMxQF/c6K/9K0ay', 1, 'e44cd884-6055-460a-9fc0-4acc664e7dba.jpg');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Índices de tabela `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Índices de tabela `evaluations`
--
ALTER TABLE `evaluations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sector_id` (`sector_id`),
  ADD KEY `class_id` (`class_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Índices de tabela `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `group_permissions`
--
ALTER TABLE `group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permission_id` (`permission_id`),
  ADD KEY `group_id` (`group_id`);

--
-- Índices de tabela `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `schools`
--
ALTER TABLE `schools`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `sectors`
--
ALTER TABLE `sectors`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD KEY `school_attended` (`school_attended`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `current_school` (`current_school`),
  ADD KEY `sector_id` (`sector_id`);

--
-- Índices de tabela `students_classes`
--
ALTER TABLE `students_classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `class_id` (`class_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Índices de tabela `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `group_id` (`group_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `classes`
--
ALTER TABLE `classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `evaluations`
--
ALTER TABLE `evaluations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `group_permissions`
--
ALTER TABLE `group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `schools`
--
ALTER TABLE `schools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `sectors`
--
ALTER TABLE `sectors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `students_classes`
--
ALTER TABLE `students_classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `classes_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `classes_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE SET NULL;

--
-- Restrições para tabelas `courses`
--
ALTER TABLE `courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL;

--
-- Restrições para tabelas `evaluations`
--
ALTER TABLE `evaluations`
  ADD CONSTRAINT `evaluations_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `evaluations_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `evaluations_ibfk_3` FOREIGN KEY (`sector_id`) REFERENCES `sectors` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `group_permissions`
--
ALTER TABLE `group_permissions`
  ADD CONSTRAINT `group_permissions_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `group_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `students_ibfk_2` FOREIGN KEY (`sector_id`) REFERENCES `sectors` (`id`),
  ADD CONSTRAINT `students_ibfk_3` FOREIGN KEY (`school_attended`) REFERENCES `schools` (`id`),
  ADD CONSTRAINT `students_ibfk_4` FOREIGN KEY (`current_school`) REFERENCES `schools` (`id`);

--
-- Restrições para tabelas `students_classes`
--
ALTER TABLE `students_classes`
  ADD CONSTRAINT `students_classes_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `students_classes_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;

--
-- Restrições para tabelas `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
