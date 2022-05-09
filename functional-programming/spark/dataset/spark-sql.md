# Spark SQL

Hadoop stocks **unstructured data**. It's easy to use, but it's hard to keep the high performance.

Therefore, **Spark SQL** comes for help. It sits on top of Spark RDD. It provides 2 things:

- build **structured data**
- improve performance

## Concepts

- relation: table
- attribute: column
- record/tuple: row

## Dataframe

It's the core of Spark SQL. It's like a **table**. There are some features about it.

- Dataframe is RDD full of records with **a schema**.

- Dataframe is **untyped**.

- Transformation on dataframe is **untyped**.

## Create a dataframe

Similar to `SparkContext`, Spark SQL starts with `SparkSession`.

There are 2 ways to create a dataframe.

- create a dataframe from RDD

  ```scala
  val tupleRDD: RDD[(String, Int)] = ???
  val tupleDF = tupleRDD.toDF("name", "age") // column names
  ```

  Case class makes it easier.

  ```scala
  case class Person(name: String, age: Int)

  val peopleRDD: RDD[Person] = ???
  val peopleDF = peopleRDD.toDF
  ```

  It's possible to create custom schema, too.

- create a dataframe from source

  Spark supports `json`, `csv`, etc.

  ```scala
  val df = spark.read.json("./names.json")
  ```

## Query a dataframe

First, we need to **register the dataframe as a temporary SQl view**.

```scala
peopleDF.createOrReplaceTempView("people")
```

Then, write a query.

```scala
val adultsDF = peopleDF
  .spl("SELECT * FROM people WHERE age > 17")
```

The statements available are largely in **HiveQL**.
