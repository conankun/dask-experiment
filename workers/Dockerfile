FROM ubuntu:20.04

RUN apt-get update

RUN apt-get install -y python3-pip

RUN python3 -m pip install dask

RUN python3 -m pip install dask[array]

RUN python3 -m pip install dask[distributed]

EXPOSE 8282

CMD dask-worker --worker-port=8282 $(echo ${SCHEDULER_ADDRESS}:${SCHEDULER_PORT})