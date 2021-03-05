FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y git python3-pip python3-dev build-essential

WORKDIR /tmp/pygeoda

COPY . .

RUN python3 setup.py install 

RUN python3 setup.py build_ext --inplace
RUN python3 -m unittest