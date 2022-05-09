# Distributed Data-Parallel

Distributed data parallelism will:

1. split data over **several nodes**
2. Node **independently** works on the data in **parallel**.
3. combine the results when done (optional)

Since there are several nodes work together, we need to wrong about the **network latency** among the nodes.

## Concerns

- Partial failure

  There is a crash of a subset of the machines.

- Latency

  Certain operations cost more time than others due to the network communication.

  This issue exists all kinds of the distribution.

## Why Spark

Spark

- retains the fault-tolerance

  Spark replays functional transformations, like Scala collections, over orignal dataset.

- reduces the latency

  Spark keeps all the data **immutable and in-memory**.

As the result, Spark is **100 times more performant** than its precedent, Hadoop. 

Spark has more APIs to use. Hadoop is basicaly a MapReduce.