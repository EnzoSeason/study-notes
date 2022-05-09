# Clusters

Let's understand how Spark works.

1. We interact with **Driver program**, which create the `SparkContext`.

2. `SparkContext` connects to a **cluster manager**, e.g., Mesos/YARN, which allocate the resources.

3. Spark acquires the **nodes in the cluster**. Each node has an executor to run the code and save the data.

4. Driver program sends your codes to the executors.

5. `SparkContext` sends tasks for executors to run.


```
Driver program
|
Cluster manager
|
| -- | -- | -- | ...
node node node ...
```

**Transaction** is executed on **Driver program**, while **action** is directly run on **executor**.