# Создание таблицы user_list с тремя столбцами: id, name и surname.
CREATE TABLE `user_list` ( 
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8; # Используется движок InnoDB и кодировка символов utf8.

# Вставка трех строк данных в таблицу user_list с указанными значениями для столбцов id, name и surname.
INSERT INTO `user_list` (`id`, `name`, `surname`) VALUES
(1, 'Pancho', 'Villa'),
(2, 'Salvatore', 'Giuliano'),
(3, 'Sultana', 'Daku');

# Добавление первичного ключа для столбца id в таблице user_list.
ALTER TABLE `user_list`
  ADD PRIMARY KEY (`id`);

# Изменение столбца id в таблице user_list
ALTER TABLE `user_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4; # Задание начального значения для автоинкремента

# Подтверждение транзакции.
COMMIT;
