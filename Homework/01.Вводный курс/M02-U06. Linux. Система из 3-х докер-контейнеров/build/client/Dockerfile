# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Устанавливаем метаданные для образа
LABEL Yura Shamray

# Обновляем пакеты внутри образа
RUN apt update && apt upgrade -y

# Устанавливаем пакет MySQL Server внутри образа
RUN apt install mysql-server -y
