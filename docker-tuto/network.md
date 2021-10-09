#  Network

In docker:

- Each container attaches to a virtual network

- The containers in the same virtual network can talk to each other

- Virtual network can connect to the host by `-p`. By default, externally exposed ports are closes.


# #  Create a network

`docker network create <my_net>`

Network driver is `bridge` by default.

# #  Create a container in a custom network

`docker container run -d --name <my_container> --network <my_net> <image>`

