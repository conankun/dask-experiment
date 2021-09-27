FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update

RUN apt-get install -y python3-pip

RUN python3 -m pip install dask

RUN python3 -m pip install dask[array]

RUN apt-get install -y ssh

RUN python3 -m pip install dask[distributed]

RUN python3 -m pip install asyncssh

RUN service ssh start

EXPOSE 22

COPY main.py main.py

CMD python3 main.py
