## Data

### Volumes

Volumes is a place to persist data.

If the container is destroyed, the data in volumes will be perserved. If we need to remove a volume, we need to delete it manually.
#### named volume

Docker will create a place on the host for the volume. Usually, we will give a volume a name.

In `docker container run`, we can use `-v`:

- create a new volumes for the container

- use an existed volumes

example: `-v <custom_name>:<container_path>`

#### bind mounts

With bind mounts, we control the exact mountpoint on the host.

We can use this to persist data, but is often used to **provide additional data** into containers.

`-v <host_path>:<container_path>` will bind mount host files in container. Always host file overrides container files.