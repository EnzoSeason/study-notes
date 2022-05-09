# Partitioning

Partitioning is the way to split data into different machines.

Properties of partitions:

- Partitions **never span multiple machines**.

  For example, tuples in the same partition must be in the same machine.

- Each machine contains **one or more** partitions.

- The number of partitions is configurable.

There are two partitioning in Spark:

- **Hash** partitioning
- **Range** partitioning

## Hash partitioning

Hash partitioning tries to spread data **evenly** across the partitions based on **key**.

For the tuple `(k, v)`, the partition will be decided by:

```scala
val p = k.hashCode() % numPartitions
```

## Range partitioning

Using a range partitioner, keys are partitioned according to:

1. an ordering for keys
2. a set of sorted ranges of keys

For example, we have the keys, `List(1, 201, 420, 460, 600)`. We can spread them by a set of ranges: `Range(1, 200), Range(200, 400), Range(400, 800)`

## Apply custom partitioning in Spark

```scala
val pairs = purchaseRdd.map(p => (p.id, p.price))
```

### partitionBy

```scala
val rangePartitioner = new RangePartitioner(8, pairs) // Spark will figure out the best partitions for us.
val partitioned = pairs.partitionBy(rangePartitioner).persist()
```

`persist()` here is important. We don't want to partition the data again and again. It's better to keep it in the memory.

### Transformation

- Some transformation will partition the data **automatically**.

  For example, `sortByKey` used **range partitioning** by default, and `groupbyKey` use **hash partitioning**.

  Other transformations are `join` (and 2 other outer join), `reduceByKey`, `groupWith`, `foldByKey`, `combineByKey`, etc.

- Some transformations will partition the data \*_only if it's applied on a partitioned RDD_.

  For example, `mapValues`, `flatMapValues`, `filter`.

- Some transformations won't parition.

  e.g. `map`, `flatMap`. These transformation may **change the keys**. That's why they won't partition.

  > Attention: If we apply these transformations on partitioned RDD, the partitions will lose!


## Advantage of partitioning

Partitioning will boost up the performance.

Previously, we compared that `reduceByKey` improves the performance by **reducing on the same node before shuffling**.

Partitioning shares the same idea. It **reduces shuffling**, too.

Therefore, the best practice is **applying `reduceByKey` on partitioned RDD**.

```scala
val cost = purchases
  .map(p => (p.id, (1, p.price)))
  .reduceByKey((a, b) => (a._1 + b._1, a._2 + b._2))
  .count()

// Command took 4.65s
```

```scala
val rangePartitioner = new RangePartitioner(8, purchases)
val partitionedPurchases = purchases.partitionBy(rangePartitioner).persist()

val cost = partitionedPurchases
  .map(p => (p.id, (1, p.price)))
  .reduceByKey((a, b) => (a._1 + b._1, a._2 + b._2))
  .count()

// Command took 1.79s
```

Partitioning is almost 4 times faster.