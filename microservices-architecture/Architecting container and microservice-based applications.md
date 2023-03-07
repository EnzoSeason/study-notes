## Container design principles

When you design a container image, you'll see an [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) definition in the Dockerfile. This definition defines the **process** whose lifetime controls the lifetime of the **container**.

If the process fails, the container ends, and the **orchestrator** takes over. If the orchestrator was configured to keep five instances running and one fails, the orchestrator will create another container instance to replace the failed process.

## Containerizing monolithic applications
![[mono-containerized-app.png]]
The downside of this approach becomes evident if the application grows, requiring it to **scale**. In most cases, just a few parts of the application are the choke points that require scaling, while other components are used less.

### Manage state and data in Docker applications
From Docker:
- **Volumes** are stored in an area of the host filesystem that's managed by Docker.
- **Bind mounts** can map to any folder in the host filesystem, so access can't be controlled from Docker process and can pose a security risk as a container could access sensitive OS folders.
- **tmpfs mounts** are like virtual folders that only exist in the host's memory and are never written to the filesystem.
From remote storage:
-   [Azure Storage](https://azure.microsoft.com/documentation/services/storage/), which provides geo-distributable storage, providing a good long-term persistence solution for containers.
-   Remote relational databases like [Azure SQL Database](https://azure.microsoft.com/services/sql-database/) or NoSQL databases like [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction), or cache services like [Redis](https://redis.io/).

#### Service-oriented architecture (SOA)
SOA means that you structure your application by decomposing it into multiple services.

### Microservices architecture
It's an approach to building a server application as **a set of small services**.
Each service **runs in its own process** and **communicates with other processes using protocols** such as HTTP/HTTPS, WebSockets.
Each microservice implements a specific end-to-end domain or business.  Each microservice should own its related **domain data model and domain logic**.
![[ms-vs-mono.png]]
The following are important aspects to enable success in going into production with a microservices-based system:

- Monitoring and health checks of the services and infrastructure.
- Scalable infrastructure for the services (that is, cloud and orchestrators).
- Security design and implementation at multiple levels: authentication, authorization, secrets management, secure communication, etc.
- Rapid application delivery, usually with different teams focusing on different microservices.
- DevOps and CI/CD practices and infrastructure.