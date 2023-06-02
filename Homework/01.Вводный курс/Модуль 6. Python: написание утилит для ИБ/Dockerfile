# Используется базовый образ Python версии 3.8.10
FROM python:3.8.10
# Установка рабочей директории внутри контейнера на /app
WORKDIR /app
# Копирование файлов и директорий из текущего рабочего каталога внутрь контейнера
COPY . /app
# Установка зависимостей Python из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Открытие порта 3000 в контейнере
EXPOSE 3000 
# Установка точки входа для запуска команды python3
ENTRYPOINT ["python3"]
# Аргументы командной строки для выполнения файла server.py
CMD ["server.py"]
