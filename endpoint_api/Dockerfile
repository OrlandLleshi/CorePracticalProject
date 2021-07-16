# Dockerfile for a Python App
FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["python", "app.py"] 