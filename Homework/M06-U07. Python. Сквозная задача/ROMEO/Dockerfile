FROM python:3.8.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python3"]
CMD ["server.py"]
