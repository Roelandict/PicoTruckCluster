FROM python:3.15.0a1-alpine3.22

WORKDIR /app
COPY app/IoTManager/ README.md /app/
RUN pip install -f requerments.txt
