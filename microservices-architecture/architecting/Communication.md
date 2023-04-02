# Communication

The microservice community promotes the philosophy of "smart endpoints and dumb pipes" This slogan encourages a design that's as decoupled as possible between microservices, and as cohesive as possible within a single microservice.

The two commonly used protocols are

- HTTP request/response with resource APIs (when querying most of all)
- lightweight asynchronous messaging when communicating updates across multiple microservices.

## Communication styles

There are many protocols and choices you can use for communication, depending on the communication type you want to use. 

If you're using a **synchronous request/response-based** communication mechanism, protocols such as **HTTP and REST approaches** are the most common, especially if you're publishing your services outside the Docker host or microservice cluster. 

If you're communicating **between services internally** (within your Docker host or microservices cluster), you might also want to use **binary format communication mechanisms** (like WCF using TCP and binary format). Alternatively, you can use asynchronous, message-based communication mechanisms such as AMQP.
