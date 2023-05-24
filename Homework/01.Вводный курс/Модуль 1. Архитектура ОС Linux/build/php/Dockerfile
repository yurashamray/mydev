# Используется базовый образ PHP версии 7.4 с Apache
FROM php:7.4-apache

# Устанавливает метку для контейнера
LABEL Yura Shamray

# Обновление пакетов внутри контейнера и установка расширений PHP
RUN apt-get update && \
    docker-php-ext-install mysqli pdo pdo_mysql
