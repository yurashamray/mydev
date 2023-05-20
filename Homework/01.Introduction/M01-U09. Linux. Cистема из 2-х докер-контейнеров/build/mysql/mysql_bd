CREATE TABLE `user_list` (
  `id` int(11) NOT NULL, -- Создание столбца 'id' типа int, который не может быть NULL
  `name` varchar(255) NOT NULL, -- Создание столбца 'name' типа varchar с максимальной длиной 255, который не может быть NULL
  `surname` varchar(255) NOT NULL -- Создание столбца 'surname' типа varchar с максимальной длиной 255, который не может быть NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8; -- Установка типа хранилища InnoDB и кодировки символов UTF-8 по умолчанию

INSERT INTO `user_list` (`id`, `name`, `surname`) VALUES -- Вставка данных в таблицу 'user_list'
(1, 'PANCHO', 'VILLA'), -- Значения для первой строки
(2, 'SALVATORE', 'GIULIANO'), -- Значения для второй строки
(3, 'SULTANA', 'DAKU'); -- Значения для третьей строки

ALTER TABLE `user_list`
  ADD PRIMARY KEY (`id`); -- Добавление первичного ключа на столбец 'id' в таблице 'user_list'

ALTER TABLE `user_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4; -- Изменение столбца 'id' для автоматического инкремента начиная с 4
COMMIT; -- Завершение транзакции
