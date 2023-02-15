CREATE TABLE `user_list` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user_list` (`id`, `name`, `surname`) VALUES
(1, 'PANCHO', 'VILLA'),
(2, 'SALVATORE', 'GIULIANO'),
(3, 'SULTANA', 'DAKU');

ALTER TABLE `user_list`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `user_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;
