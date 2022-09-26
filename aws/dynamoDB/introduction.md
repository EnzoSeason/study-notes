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

-  If we choose strongly consistent, then we are choosing the consistency and partition tolerance, and **our availability will suffer in the response times**.

-  If we choose the highest levels of availability, then we are choosing availability and partition tolerance, and **our consistency will be eventual instead of strong**.
