<?php

error_reporting(E_ALL); // Включение вывода всех ошибок

$link = mysqli_connect("mysql", "root", "secret123", "mifiib"); // Подключение к MySQL серверу

if (mysqli_connect_errno()) {
    printf("Can't connect to: %s\n", mysqli_connect_error()); // Вывод сообщения об ошибке подключения
    exit(); // Завершение выполнения скрипта
}

$data = '';

if ($result = mysqli_query($link, "SELECT * FROM user_list")) { // Выполнение запроса к базе данных
    while ($row = $result->fetch_assoc()) {
        //echo $row['id'].' - '.$row['name'].' - '.$row['surname'].'<br>'; // Вывод данных каждой строки результата
		
		$data.= "<tr><td>".$row['id']."</td><td>".$row['name']."</td><td>".$row['surname']."</td></tr>"; // Формирование строки данных для вывода
    }
}

$html = '
	<style>.users { padding: 0; margin: 0 auto; border: 1px solid #000; color: #000; border-collapse: collapse; } .users th { text-align: left; } .users td { padding: 5px; font-size: 14px; }</style>
	<h1 style="text-align: center;">THE STUDENTS LIST (MIFIIB)</h1>
	<table class="users" padding="0" cellspacing="0"><tr><th width="100">ID</th><th width="300">Name</th><th width="300">Surname</th></tr>'.$data.'</table>
';

echo $html; // Вывод сформированной HTML-таблицы

phpinfo(); // Вывод информации о PHP-конфигурации

?>
