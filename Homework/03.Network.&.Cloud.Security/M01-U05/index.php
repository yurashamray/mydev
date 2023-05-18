<?php

error_reporting(E_ALL);

# Загрузка значения адреса сервера из файла mifiib-config.yaml
$configFile = 'mifiib-config.yaml';
$config = yaml_parse_file($configFile);
$databaseServer = $config['data']['mifiib-url'];

# Загрузка значений логина и пароля из файла mifiib-secret.yaml
$secretFile = 'mifiib-secret.yaml';
$secret = yaml_parse_file($secretFile);
$databaseUsername = base64_decode($secret['data']['username']);
$databasePassword = base64_decode($secret['data']['password']);
$dbName = 'mifiib';
$link = mysqli_connect($databaseServer, $databaseUsername, $databasePassword, $dbName);

if (mysqli_connect_errno()) {
    printf("Can't connect to: %s\n", mysqli_connect_error());
    exit();
}

$data = '';

if ($result = mysqli_query($link, "SELECT * FROM user_list")) {
    while ($row = $result->fetch_assoc()) {
        //echo $row['id'].' - '.$row['name'].' - '.$row['surname'].'<br>';
		
		$data.= "<tr><td>".$row['id']."</td><td>".$row['name']."</td><td>".$row['surname']."</td></tr>";
    }
}

$html = '
	<style>.users { padding: 0; margin: 0 auto; border: 1px solid #000; color: #000; border-collapse: collapse; } .users th { text-align: left; } .users td { padding: 5px; font-size: 14px; }</style>
	<h1 style="text-align: center;">The Students List (MIFIIB)</h1>
	<table class="users" padding="0" cellspacing="0"><tr><th width="100">ID</th><th width="300">Name</th><th width="300">Surname</th></tr>'.$data.'</table>
';

echo $html;

phpinfo();

?>
