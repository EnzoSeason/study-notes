## Challenges

### How to define the boundaries of each microservice

Focus on the application's **logical domain models** and **related data**. The contexts should be defined and managed independently. You always attempt to **minimize the coupling** between those microservices.

### How to create queries that retrieve data from several microservices

1. **API Gateway**: It's for **simple data aggregation** from multiple microservices.  Be careful about implementing this pattern, because it can be a **choke point** in your system.
2. **CQRS with query/reads tables**: Another solution for **aggregating data from multiple microservices**. You generate, **in advance** (prepare denormalized data before the actual queries happen), a **read-only table** with the data that's owned by multiple microservices, instead of a complex join of multi-tables. However, CQRS with query/reads tables means **additional development work**, and you'll need to **embrace eventual consistency**.
3. **"Cold data" in central databases**: For complex reports and queries that **might not require real-time data**, a common approach is to export your "hot data" (transactional data from the microservices) as "cold data" into large databases that are used only for reporting.

### How to achieve consistency across multiple microservices

To make an update to the different microservices should use **eventual consistency** probably based on **asynchronous communication** such as integration events (message and event-based communication).

As stated by the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem), you need to choose between **availability** and ACID strong **consistency** (Partition tolerance is a must). Mission-critical applications must remain up and running, and developers can work around strong consistency by using techniques for working with **weak or eventual consistency**. It's a common approach.

This challenge is also related to the question of how to propagate changes across multiple microservices when certain data needs to be **redundant**.

A good solution for this problem is to use eventual consistency between microservices articulated through **event-driven communication** and a **publish-and-subscribe system**.

### How to design communication across microservice boundaries
In this context, communication doesn't refer to what protocol you should use (HTTP and REST, AMQP, messaging, and so on). Instead, it addresses what communication style you should use, and especially **how coupled your microservices should be**. Depending on the level of coupling, when failure occurs, **the impact of that failure** on your system will vary significantly.

In a distributed system like a microservices-based application, with so many artifacts moving around and with distributed services across many servers or hosts, **components will eventually fail**. So you need to **design your microservices and the communication across them** considering the common risks.

A popular approach is to implement **HTTP (REST)-based microservices,** due to their **simplicity**. It's okay for simple interaction between microservices and API Gateway or client apps, but it's **terrible for long chains of synchronous HTTP calls across microservices**. There are important points to consider when going down this path:
- Blocking and low performance
- Coupling microservices with HTTP
- Failure in any one microservice

Therefore, in order to enforce microservice autonomy and have better resiliency, you should **minimize the use of chains of request/response communication across microservices**. It's recommended that you u**se only asynchronous interaction for inter-microservice communication**, either by **using asynchronous message- and event-based communication**, or by **using (asynchronous) HTTP polling** independently of the original HTTP request/response cycle.

## Identify domain-model boundaries for each microservice

The goal should be to get to the **most meaningful separation** guided by your **domain knowledge**. **Cohesion** is a way to identify how to break apart or group together microservices.

To identify bounded contexts, you can use a DDD pattern called the [Context Mapping pattern](https://www.infoq.com/articles/ddd-contextmapping). A BC is **autonomous** and includes **the details of a single domain** -details like the domain entities- and defines **integration contracts with other BCs**.

When designing a large application, developers **accept the differences and richness** provided by each domain, not try to unify them.

![identifying-domain-model.png](../images/identifying-domain-model.png)
However, you might also have entities that have a different shape but share the same identity across the multiple domain models from the multiple microservices.
![decomposing-into-domain-models.png](../images/decomposing-into-domain-models.png)
Basically, there's a **shared concept** of a user that exists in multiple services (domains), which all share the identity of that user. But in each domain model there might **be additional or different details** about the user entity. The benefits are:
- reduce duplication
- having a **primary microservice** that owns a certain type of data per entity so that updates and queries for that type of data are driven only by that microservice.

## API gateway pattern vs Direct client-to-microservice communication

### Direct client-to-microservice communication

![direct-client-communication.png](../images/direct-client-communication.png)

In this approach, **each microservice has a public endpoint**, sometimes with a different TCP port for each microservice.

In production environments, you could have an Application Delivery Controller (ADC) like [Azure Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-introduction) **between your microservices and the Internet**. This layer acts as a transparent tier that not only performs load balancing, but secures your services by offering SSL termination.

A direct client-to-microservice communication architecture could be good enough for **a small microservice-based application**, especially if the client app is a server-side web application like an ASP.NET MVC app. Consider the following questions when developing a large application based on microservices:
-  _How can client apps minimize the number of requests to the back end and reduce chatty communication to multiple microservices?_
-  _How can you handle cross-cutting concerns such as authorization, data transformations, and dynamic request dispatching?_ API Gateway is a place to handle them.
- _How can client apps communicate with services that use non-Internet-friendly protocols?_ Requests must be performed through protocols like HTTP/HTTPS and translated to the other protocols afterwards
- _How can you shape a facade especially made for mobile apps?_ API Gateway is a choice.

### Why consider API Gateways instead of direct client-to-microservice communication

-   **Coupling**: Without the API Gateway pattern, the client apps are coupled to the internal microservices. The client apps need to know how the multiple areas of the application are decomposed in microservices.
 
-   **Too many round trips**: A single page/screen in the client app might require several calls to multiple services.

-   **Security issues**: Without a gateway, all the microservices must be exposed to the "external world", making the attack surface larger than if you hide internal microservices that aren't directly used by the client apps.

-   **Cross-cutting concerns**: Each publicly published microservice must handle concerns such as authorization and SSL.

### API Gateway

This pattern is a service that provides a **single-entry point** for certain groups of microservices. The API Gateway pattern is also sometimes known as the "backend for frontend" ([BFF](https://samnewman.io/patterns/architectural/bff/)) because you build it while thinking about the needs of the client app.

Therefore, the API gateway sits between the client apps and the microservices. It acts as a **reverse proxy, routing requests** from clients to services. It can also **provide other cross-cutting features** such as authentication, SSL termination, and cache.

![single-api-gateway.png](../images/single-api-gateway.png)

That fact can be an important risk because your API Gateway service will be growing and evolving based on many different requirements from the client apps. That's why it's very much recommended to **split the API Gateway in multiple services or multiple smaller API Gateways**, one per client app form-factor type, for instance.

![multi-api-gateways.png](../images/multi-api-gateways.png)

Drawbacks of API Gateway:
- Coupling that tier with the internal microservices
- An additional possible single point of failure
- An API Gateway can introduce increased response time due to the additional network call.
- If not scaled out properly, the API Gateway can become a bottleneck.
- An API Gateway requires additional development cost and future maintenance if it includes **custom logic and data aggregation**.
- If the API Gateway is developed by a single team, there can be a development bottleneck. We can have **several fined-grained API Gateways** or **segregate the API Gateway internally** into multiple areas or layers owned by different teams working on the internal microservices.

