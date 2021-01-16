FROM python:2.7.11-alpine as base

#FROM ubuntu:18.04

#MAINTANER Your Name "slava.bikov@gmail.com"

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app

#ENTRYPOINT [ "python" ]

FROM base as test

RUN pip install --upgrade pip && \
    pip install pytest

COPY ./tests /tests

WORKDIR /tests

RUN pytest -v test_hello_world.py

FROM base

EXPOSE 5000

CMD [ "python", "hello.py" ]

