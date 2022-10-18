FROM python:3.10-alpine

COPY ./requirements.txt /requirements.txt
RUN apk update
RUN apk add --virtual build-dependencies
RUN apk add build-base
RUN apk add python3-dev


RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./src /app