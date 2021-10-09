#  Docker Compose

# #  docker-compose.yml

```yaml
version: "3.9" #  optional since v1.27.0
services: #  containers, same as docker run
  service1: #  a custom name, it's also the DNS name inside network
    image: # optional
    command: # optional
    volumes: # optional, same as -v
    environment: # optional, same as -e
  service2:
    depends_on: 
      - service1

volumes: # optional
networks: # optional
```

# # #  add image build

docker-compose can build a custom image, too.

```yaml
services:
  myService:
    build:
      context: .
      dockerfile: my.Dockerfile
    image: my-image 
```

# #  CLI

`docker-compose` is perfect for dev / test tasks. It can build and destroy the env quickly.

- `docker-compose up`: build and run the container

 - `docker-compose down`: stop and remove the constainer / network

   - to remove the volumes, use `-v`