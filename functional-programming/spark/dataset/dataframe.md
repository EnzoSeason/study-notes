# Dataframe

Dataframe is the RDD with schema. It stores structured data.

## Transformations

```scala
def select(col: String, cols: String*): Dataframe
// select a part of the dataframe and return it as a new one
```

```scala
def agg(expr: Column, expr: Column*): Dataframe
// aggregate columns and return a new dataframe
```

```scala
def groupBy(col: String, cols: String*): Dataframe
// group the dataframe on columns
// It's intended to be used before agg.
```

```scala
def join(df: Dataframe): Dataframe
// inner join with another dataframe
```

### Column

There are 3 ways to work with columns.

- `$` notation

  ```scala
  import spark.implicits._

  df.filter($"age" > 17)
  ```

- dataframe referring

  ```scala
  df.filter(df("age") > 17)
  ```

- sql string (not recommanded)

  ```scala
  df.filter("age > 17")
  ```

## Basic query

```scala
val sydneyPeopleDF = peopleDF
  .select("id", "name")
  .where($"city" == "Sydney") // where and filter are the same.
  .orderBy("id")
```

```scala
val sydneyAdultsDF = peopleDF
  .select("id", "name")
  .filter(($"city" == "Sydney") && ($"age" > 17))
  .orderBy("id")
```

## Grouping and Aggregating

```scala
val mostExpensiveDF = itemsDF
  .groupBy($"name")
  .max("price")
```

```scala
val ranksDF = postsDF
  .groupBy($"authorId", $"topicId")
  .agg(count($"authorId")) // return new dataframe whose columns are authorId, topicId, count(authorId)
  .orderBy($"topicId", $"count(authorId)".desc) // order by, first, topicId, then count(authorId) in desc.
```

## Clean data

drop the data

- `drop()`

  drop the row if it has any `null` or `NaN`.

- `drop("all")`

  drop the row if all its items are `null` or `NaN`.

- `drop(Array("id"))`

  drop the row if its `id` is `null` or `NaN`.

replace the data

- `fill(0)`

  replace all `null` or `NaN` by `0`

- `fill(Map("balance" -> 0))`

  replace `null` or `NaN` of _balance_ by `0`

- `replace(Array("id"), Map("1" -> "001"))`

  replace `1` in the column `id` by `001`
