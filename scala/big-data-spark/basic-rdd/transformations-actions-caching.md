# Transformations, Actions, Caching

## Recall

In Scala sequential collections, we have:

- Transformer

  It returns **new collections**.

- Accessor

  It returns **single values**.

## Basic

In Spark, we have:

- Transformation

  It returns **new RDDs**. It's **lazy**.

- Action

  It return the **computed results of RDDs**. It's **eager**.

It's very important that **transform is lazy and action is eager**. It's how Spark reduces the network latency.

For example, if we apply `map` on a RDD:

```scala
// use parallelize function of SparkContext(sc)
// to create a RDD from a Scala collection
val wordsRDD = sc.parallelize(largeList)
val lengthsRDD = wordsRDD.map(_.length)
```

Nothing happens on the clusters yet. `lengthsRDD` is just a reference. The actual compution is invoked only by **actions**.

```scala
val totalLength = lengthsRDD.reduce(_ + _)
// Now, the map function runs on the clusters,
// and the total length is computed.
```

## Common functions

- Transformations (lazy)

  - map

  - flatMap

  - filter

  - distinct

    get the distincts element from RDD.

- Actions (eager)

  - collect

    return all the elements of RDD

  - count

    return the number of elements in RDD

  - take

    return first `n` elements of RDD

  - reduce

    combine all the elements in RDD

  - foreach

    apply a function on each element of RDD

## Caching

So far, we have discussed the common points between Spark and Scala collection. Now, let's talk about a main difference between these two, caching.

Spark allows user to cache the data in memory to improve the performance.

We use `persist()` to cache data.

```scala
val logs = largeLogs.filter(_.contains("error")).persist()
val firstLogs = logs.take(10)
```

In this case, after `firstLogs` is computed, Spark will cache `logs` for faster future access.
