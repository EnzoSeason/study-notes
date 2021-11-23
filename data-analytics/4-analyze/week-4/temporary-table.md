# Temporary table

A temporary table is a database table that is created and exists temporarily on a database server. It stores subsets of data from standard data tables for a certain period of time.

Data analyst want to perform calculations on a small subset of the table. Rather than filtering the data over and over, they create a temporary table.

By using a temporary table, you were able to **answer a more complex question** and **not make any changes to a primary table** in the database.

## WITH (SQL)

We use `WITH` to create a temporary table.

```sql
WITH
  longest_used_bike AS (
  SELECT
    bikeid,
    SUM(duration_minutes) AS trip_duration
  FROM
    `bigquery-public-data.austin_bikeshare.bikeshare_trips`
  GROUP BY
    bikeid
  ORDER BY
    trip_duration DESC
  LIMIT
    1 )

## find the station at which the longest ride start

SELECT
  trips.start_station_id,
  COUNT(*) AS trips_ct
FROM
  longest_used_bike AS longest
FULL JOIN
  `bigquery-public-data.austin_bikeshare.bikeshare_trips` AS trips
ON
  longest.bikeid = trips.bikeid
GROUP BY
  trips.start_station_id
ORDER BY
  trips_ct DESC
LIMIT
  1
```

## SELECT INTO (SQL)

`SELECT INTO` is another way to create a temporary table.

```sql
SELECT
  *
INTO
  AfricaSales
FROM
  GlobalSales
WHERE
  region = "Africa"
```

## CREATE TABLE (SQL)

CREATE TABLE statement will create a table and save it in the database.

After you have finished working with the table, you would then **delete or drop it from the database** at the end of your session.

```sql
CREATE TABLE table_name(
  column_name_1 datatype,
  column_name_2 datatype,
  ...
)

DROP TABLE table_name
```

## Best practices when working with temporary tables

- **Global vs. local temporary tables**:

  Global temporary tables are made available to all database users and are deleted when **all connections** that use them have closed.

  Local temporary tables are made available **only to the user** whose query or connection established the temporary table.

  You will most likely be working with local temporary tables. If you have created a local temporary table and are the only person using it, you can drop the temporary table after you are done using it.

- **Dropping temporary tables after use**:

  Dropping a temporary table not only removes the information contained in the rows of the table, but **removes the table variable definitions (columns) themselves**.

  Deleting a temporary table removes the rows of the table but **leaves the table definition and columns ready to be used again**. Although local temporary tables are dropped after you end your SQL session, **it may not happen immediately**.

  If a lot of processing is happening in the database, **dropping your temporary tables** after using them is a good practice to keep the database running smoothly.
