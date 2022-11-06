# Basic knowledge

## SLA (Service-Level Agreement)

It's a service commitment given by the Provider to the Customer.

There are some important indicators.

### Availabilty

Availability refers to the percentage of time that system services are up and running.

For example, **99.99% availabilty** means the system can be down about **8.6 seconds per year** (24 \* 60 \* 60 \* 0.0001).

### Accuracy

Accuracy refers to whether **some data is allowed to be inaccurate or lost** in the system services we design.

**Error rate** is used to measure the accuracy, and the error rate is `Nb of Validated requests with Internal Error response` / `Nb of all the request`.

**Perfomance Test** and **Log** are used to get the error rate.

### Capacity

System capacity usually refers to **the expected amount of load** that the system can support.

**QPS (Queries Per Second)** or **RPS (Requests Per Second)** is used to measure it.

There are two ways to define QPS.

- **Throttling**

  For each server, we give a throttle. Then, the QPS of the system should be `Nb of servers` \* `throttle`.

  Be careful about the limit of memory when we set the throttle. We shoud avoid **Out-Of-Memory**.

- **Performance Test**

  We can test the QPS in test environment.

  If the developer use the same request parameter, system will **hit the cache**. Then the performance test doesn't represent the real case.

### Latency

Latency refers to **the time interval between when the system receives a user's request and responds to the request**.

In SLA, **p95** or **p99** indicates the latency level. If p95 means **1s**, then in 100 requests, at least 95 requests has less than 1s response time.

In order to reduce the latency, we will put data in **cache**. We can get the **Cache Hit Ratio** after running the system for a while.

## Important indicators for distributed system

Besides the indicators of SLA, there are other important indicators for distributed system.

### Scalability

There are 2 ways to scale up the system:

- Horizontal Scaling: Add more servers

- Vertical Scaling: Upgrade the server

Horizontal Scaling is more widely used. It improves system's availabilty. However, overuse it will make managing the servers hard. What's more, the relational database is hard to apply horizontal scaling because **its tables are usually joined**. Therefore, NoSQL is more suitable for horizontal scaling.

### Consistency

Consistency makes sure all the servers in the system have the same data.

There are 3 types of consistency:

- Strong consistency

  After data is written into a node, all the nodes are updated. Therefore, all the nodes in the system have the same data **at any moment**.

- Weak consistency

  After data is written into a node, other nodes will be updated **in a while**.

- Eventual consistency

  It's a type of weak consistency. If there is no new update, all accesses are to the last updated value **eventually**.

Strong consistency will cost latency. In real word, most of the distributed systems apply eventual consistency.

### Data Durability

It means once data is saved in the system, it can be used all the time, no matter node offline/downtime or data corruption.

To improve data duability, we usually **copy data into different nodes**.

Besides, distributed system requires **message durability**. The messages passed among nodes shouldn't be lost. We use **distributed message service**, such as Kafka, RabbitMQ, to reach it. Message durability includes:

- When an error occurs on the node of the message service, the message that has been sent will still be processed after the error is resolved.

- If a message queue declares persistence, even if the queue goes offline after the message is sent, it will still receive the message when it comes back online.

## Batching vs Streaming

Data can be classified in:

- Unbouded data: aka. streaming data. e.g. signal sent by sensor

- Bounded data: e.g. data in a csv file

Data has time domain problem:

- Event time: the moment that data is created

- Processing time: the moment that data is received by system

### Batching

Batching takes care of **bounded data**, and cares about **event time**. It's used for:

- Log analysis: create a daily/weekly/yearly report to get the system performance

- Data warehouse: anaylze the data by event time and create a daily/weekly/yearly report

Hadoop or Spark is created for batching processing.

### Streaming

Streaming takes care of **unbounded data**. It cares about both **evene time** and **processing time**.

- To analyze QPS of a website, it cares about **processing time**.

- To analyze the data of a medical system, it cares about **event time**.

Streaming has **low latency**. If the latency is at **milisecond** level, it's a **real-time processing**.

Therefore, it's used for:

- real-time monitoring: capture and analyze the data fron sensors, news sources, clicks, etc.

- real-time business intellegent: smart car, smart home, smart medical care, etc.

- POS system: stock trading, real-time transaction, etc.

Kafka, Flink, Beam, etc. are created for streaming processing.
