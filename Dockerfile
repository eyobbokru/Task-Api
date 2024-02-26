FROM python:3.13-rc-alpine3.19

ENV PYTHONUNBUFFERED 1

COPY ./requirements.text /tmp/requirements.txt 
COPY ./app  /app
WORKDIR /app
EXPOSE 8000




