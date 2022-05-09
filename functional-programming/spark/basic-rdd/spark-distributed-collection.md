# RDD: Spark distributed collection

## Resilient Distributed Datasets (RDD)

RDD is similar to **immutable** sequential Scala collection.

```scala
abstract class RDD[T] {
  def map[U](f: T => U): RDD[U]
  def flatMap[U](f: T => TraversableOnce[U]): RDD[U]
  def filter(f: T => U): RDD[U]
  def reduce(f: T => U): RDD[U]
}
```

## Create a RDD

- Transform from an existing RDD

  For example, use `map` to transform a RDD.

- Create from SparkContext (SparkSession)

  SparkContext helps you to talk to Spark. There are 2 important functions:

  - `parallelize`: It converts Scala collection to RDD.

  - `textFile`: It reads files from HDFS(Hadoop's File System), or local machine.
