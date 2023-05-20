FROM php:7.4-apache # Используется базовый образ PHP версии 7.4 с Apache
LABEL Yura Shamray # Устанавливает метку для контейнера
RUN apt-get update && \ # Обновление пакетов внутри контейнера
    docker-php-ext-install mysqli pdo pdo_mysql # Установка расширений PHP
