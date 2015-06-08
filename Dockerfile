FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-pip python-dev && apt-get clean
RUN pip install bottle
RUN pip install pymongo

WORKDIR /app
ADD . /app

CMD python hello_bottle.py
EXPOSE 8000
