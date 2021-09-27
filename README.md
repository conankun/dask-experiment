# 💨 Dask Experiment
This repository tests distributed processing for the dask
with Kubernetes locally.

# 📚 Prerequisite
- You must have Docker and Kubernetes installed in your
machine.
  
# ⬆️ How to turn up
1. In `/`,`/scheduler`, and `/workers`, use `./run.sh` to build
   docker images. If you get permission error, 
   please run `chmod 754 run.sh` and retry.
2. Use `kubectl apply` to create or update the resource in the
cluster.
   ```shell
    kubectl apply -f ./deployment.yaml
    ```
3. Expose the service `dask-test`. This will turn up the
`dask-test` in the cluster.
   ```shell
   kubectl expose deployment dask-test
   ```
4. Get the name of the pod for `dask-test` using 
   `kubectl get pods`. In this example, we will assume it's 
   `dask-test-67d7c55845-z68b5`.
4. Use `kubectl logs` to see the log. You can use the following
command to see the log of `main.py`.
   ```shell
   kubectl logs dask-test-67d7c55845-z68b5 example
   ```
   If you are getting something like the output below, you are
   good to go.
   ```text
    Starting the application
    Connected to the dask scheduler.
    171826456.18201578
    ```
5. If you want to see the log of scheduler or worker, you can
replace `example` in the above command with `scheduler` or 
   `worker`.