# Introduction

## Relational Databases and the Problem that Need Solving

The relational database management system provided a way to **normalize the data**, in order to provide a methodology for **analytical processing**. The relational database application gave a strong analytical approach for business intelligence. It provided better access and organization for the data being created, and provided a system that could be both redundant and scalable.

Another thing the relational system provided was **a trade-off of storage costs for CPU costs**. The ability to consume and normalize that data required more compute capabilities than was originally needed. Additionally, it took much more CPU power in order to take the normalized data across multiple datasets and tables, and display it based on what was being requested.

### CAP

CAP stands for **consistency, availability, and partition tolerance**.

- Consistency refers to the choice of either eventually or strongly consistent data.

  There are 2 ways to return a response of a request in the replicated and distributed system:

  - The system checks with the **replication point**, and returns the result stored at only that replication point. Depended on the replication, the data may be outdated. It's seen as **eventually consistent**.

  - The system checks across **all replication points** before returning a result. The data is up-to-date, but it's slower and more computationally expensive.

- Availability is to return a response quickly.

- Partition tolerance is the system's ability to maintain functionality, data retention, and consistency promises **through failures** of network or components.

These 3 points can't be reached at the same time, and we need **Partition tolerance** regardless of the use cases. So, our operations have to choose between consistency and availability.

- If we choose strongly consistent, then we are choosing the consistency and partition tolerance, and **our availability will suffer in the response times**.

- If we choose the highest levels of availability, then we are choosing availability and partition tolerance, and **our consistency will be eventual instead of strong**.

## NoSQL

There are some inconvenience about NoSQL.

- NoSQL databases are made up of denormalized data. Querying of normalized highly structured data can become very complex.

- NoSQL systems do not have cross-table relationships.

### Types

There are 3 main types of NoSQL:

- Key-value

  It provides large hash tables of keys and values, and give you the ability to query for items that are organized by their key structure. E.g. DynamoDB.

- Column-based

  Data is stored and optimized for **fast retrieval of a lot of data**. E.g. Cassandra.

- Document-based

  It is categorized by its ability to store documents made up of **tagged elements**. E.g. MongoDB.

### DynamoDB

- Table:

  A table is, in its most basic form, a collection of zero or more items.

- Key:

  The "prmiary" key is the **partition key**.

  There is another key, sort key. While the primary or sort key can be duplicated, you cannot duplicate the primary and sort key within the table.

- Attribute:

  It's the value associated with the key. The data type, such as String, Boolean, etc., is required.

#### Limits

- Max item size: 400 Kb

  DynamoDB is not for big data blobs. We should consider S3, instead.

- Min and Max key length

  - partition key: 1 bytes to 2048 bytes
  - sort key: 1 bytes to 1024 bytes

## Exercises

- [Creating an Amazon DynamoDB Table using
the AWS Software Development Kit (AWS SDK)](./docs/week-1-exercise-1.pdf)
