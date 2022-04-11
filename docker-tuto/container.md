## Basic


### Basic commands
#### create a container

`docker container run` (`docker run`)

Exemple:

`docker container run --publish 8080:80 nginx`

1. Find Nignx **Image** in the local / Download from the Docker Hub

2. start a **container** from the image

3. open Port `8080` on the host IP, and route the traffic to the container IP Port `80`

`--detech` run the container in the backgroud

#### see the containers

`docker container ls` (`docker ps`)

list the running containers

#### run an existed container

`docker container start  <container_id>` (`docker start`)

#### stop a container

`docker container stop <container_id>` (`docker stop`)


#### check the logs

`docker container logs`

#### list the running process of a container

`docker container top <container_name >`

#### remove a container

`docker container rm <container_id>`


#### check the config of the container

`docker container inspect <container_id>`

#### stats

`docker container stats`

#### help

`docker container --help`

### Enter container

- start a **new** container and enter it:

    `docker container run -it <container> bash`

    If we exit it, container stops

- enter a running container: 

    `docker container exec -it <container> bash`

    If we exit it, container still runs


One more useful tag: `--rm`. It causes Docker to automatically remove the container when it exits.