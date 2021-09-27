FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update

RUN apt-get install -y python3-pip

RUN python3 -m pip install dask

RUN python3 -m pip install dask[distributed]

EXPOSE 8080
EXPOSE 8787

CMD dask-scheduler --port 8080
