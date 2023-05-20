FROM python:3.8.10 # Используется базовый образ Python версии 3.8.10
WORKDIR /app # Установка рабочей директории внутри контейнера на /app
COPY . /app # Копирование файлов и директорий из текущего рабочего каталога внутрь контейнера
RUN pip install --no-cache-dir -r requirements.txt # Установка зависимостей Python из файла requirements.txt
EXPOSE 3000 # Открытие порта 3000 в контейнере
ENTRYPOINT ["python3"] # Установка точки входа для запуска команды python3
CMD ["server.py"] # Аргументы командной строки для выполнения файла server.py
