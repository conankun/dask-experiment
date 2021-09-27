# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# First you need to setup SSH permission.

# 1) Generate the sshkey using ssh-keygen -b 1024 -t rsa
# 2) Register the public key in the server using ssh-copy-id -i ~/.ssh/key.pub ${ip_address_of_server}


from dask.distributed import Client, SSHCluster
import dask.array as da
import argparse

"""
parser = argparse.ArgumentParser(description="")
parser.add_argument('-i' '--ip_addr', dest='ip_addr', nargs='+', required=True)
args = parser.parse_args()

def main() -> None:
    print(f'IP Address: {args.ip_addr}')
    cluster = SSHCluster(
        list(args.ip_addr),
        connect_options={
            'known_hosts': None,
            'username': 'eugenekim',
            'client_keys': '~/.ssh/dask'
        },
        worker_options={'nthreads': 2},
        scheduler_options={
            'port': 0,
            'dashboard_address': ':8797'
        },
    )
    Client(cluster)
    print('Finished provisioning. Starting the operations.')
    x = da.random.random((10000, 10000), chunks=(1000, 1000))
    y = da.exp(x).sum().compute()
    print(y)
"""

def main2() -> None:
    client = Client('tcp://localhost:8080')
    print('Connected to the dask scheduler.')
    x = da.random.random((10000,10000), chunks=(1000,1000))
    y = da.exp(x).sum()
    print(y.compute())


if __name__ == '__main__':
    print('Starting the application')
    main2()
