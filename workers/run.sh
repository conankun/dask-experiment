docker build -t dask-worker .
docker container run -it --env SCHEDULER_ADDRESS=172.17.0.2 --env SCHEDULER_PORT=8080 --rm dask-worker