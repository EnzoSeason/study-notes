## Container design principles

When you design a container image, you'll see an [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) definition in the Dockerfile. This definition defines the **process** whose lifetime controls the lifetime of the **container**.

If the process fails, the container ends, and the **orchestrator** takes over. If the orchestrator was configured to keep five instances running and one fails, the orchestrator will create another container instance to replace the failed process.

## Containerizing monolithic applications
![[mono-containerized-app.png]]
The downside of this approach becomes evident if the application grows, requiring it to **scale**. In most cases, just a few parts of the application are the choke points that require scaling, while other components are used less.
