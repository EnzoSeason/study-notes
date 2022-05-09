# Pair RDD

In the world of large scale data processing and distributed computing, it's actually very common to operate on data in the form of **key-value pairs**.

In single node computing, we have the data structure for it. It's `Map`.

In Spark, we have **pair RDD**.

```scala
RDD[(K, V)]
```

## Create a pair RDD

```scala
val rdd: RDD[Article] = ???

val pairRdd: RDD[(String, String)] =
  rdd.map(article => (article.title, article.texts))
```

## Transformations

- groupByKey

- reduceByKey

- mapValues

- keys

- join

- leftOuterJoin/rightOuterJoin

### groupByKey

Recall: `groupBy` in Scala collection is:

```scala
def groupBy[K](f: A => K): Map[K, Traversable[A]]
```

For example,

```scala
val ages = List(1, 10, 20, 40, 66)
val people = ages.groupBy { age =>
  if (age < 18) "child"
  else if (age >= 18 && age < 60) "adult"
  else "senior"
}

println(people)
// Map("child" -> List(1, 10), "adult" -> List(20, 40), "senior" -> List(66))
```

Now, let's see `groupByKey` of **pair RDD**.

```scala
def groupByKey(): RDD[(K, Iterable[A])]
```

For example,

```scala
// create a pair RDD
val eventsRDD = sc.parallelize(...).map(event => (event.name, event.budget))
val groupedRDD = eventsRDD.groupByKey()

groupedRDD.collect().foreach(println)
// (Adobe, CompactBuffer(1000))
// (Google, CompactBuffer(1000, 2500))
// ...
```

### reduceByKey

It combines `groupByKey` and reducing. Calling this function is more **efficient**.

```scala
def reduceByKey(f: (V, V) => V): RDD[(K, V)]
```

For example,

```scala
val budgetsRDD = eventsRDD.reduceByKey(_ + _)

budgetsRDD.collect().foreach(println)
// (Adobe, 1000)
// (Google, 3500)
// ...
```

### mapValue

It applies the function on the value of pair RDD.

```scala
def mapValues[U](f: V => U): RDD[(K, U)]
```

```scala
val doubleBudgetsRDD = eventsRDD.mapValues(_ * 2)

doubleBudgetsRDD.collect().foreach(println)
// (Adobe, 2000)
// (Google, 2000)
// (Google, 5000)
// ...
```

### Join

There are 2 kinds:

- inner join: `join`

  ```scala
  def join[W](other: RDD[(K, W)]): RDD[(K, (V, W))]
  ```

  ```scala
  val joinedRDD = leftRDD.join(rightRDD)
  ```

  The keys in `joinedRDD` must exist in both `leftRDD` and `rightRDD`.

- outer join:

  - `leftOuterJoin`

    ```scala
    def leftOuterJoin[W](other: RDD[(K, W)]): RDD[(K, (V, Option[W]))]
    ```

    ```scala
    val joinedRDD = leftRDD.leftOuterJoin(rightRDD)
    ```

    The keys in `joinedRDD` must exist in both `leftRDD`.

  - `rightOuterJoin`

    ```scala
    def rightOuterJoin[W](other: RDD[(K, W)]): RDD[(K, (Option[V], W))]
    ```

    ```scala
    val joinedRDD = rightOuterJoin.leftOuterJoin(rightRDD)
    ```

    The keys in `joinedRDD` must exist in both `rightRDD`.


## Actions

- countByKey

### countByKey

It returns a map that stores the count of each key.

```scala
def countByKey(): Map[K, Long]
```

## Exercise for transformations and actions

Calculate the average buget of each event.

```scala
val averageBudgetRDD = eventsRDD
  .mapValues(budget => (budget, 1))
  .reduceByKey((v1, v2) => (v1._1 + v2._1, v1._2 + v2._2))
  .mapValues((totalBudget, count) => totalBudget / count)
```
