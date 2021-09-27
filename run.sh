docker build -t dask-example .
docker container run -it -p 8787:8787 --rm dask-example