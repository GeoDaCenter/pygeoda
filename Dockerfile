FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y git python3-pip python3-dev build-essential \
    && pip3 install git+https://gitee.com/lixun910/pygeoda