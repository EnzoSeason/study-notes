# Index

Index makes the searching becomes faster.

There are some types of data structure used in the database engine.

- hash map: Memcached or some NoSQL

- order array: fast to search, but difficult to insert/remove

- Binary Search Tree

## InnoDB Index

InnoDB uses **B+ Tree** as the index.

## Primary key vs Key

If we use primary key to find an item in the database, we only need traverse the database **once**.

However, if we use the key other than the primary key, we need traverse to find the **primary key first**, the use the primary key to find the item.

That's the reason why we prefer using the primary key.


## Avoid re-traversing by the primary key

In the exemple, we use the table as followed

```sql

create table T (
    ID int primary key,
    k int NOT NULL DEFAULT 0, 
    s varchar(16) NOT NULL DEFAULT '',
    index k(k)
) engine=InnoDB;
```

1. only select id

    Instead of

    ```sql
    SELECT * from T WHERE between 3 and 5
    ```

    We only select the primary key. It can avoid re-traversing because the primary keys are in the B+ Tree of the keys.

    ```sql
    SELECT ID from T WHERE between 3 and 5
    ```

    Because of this feature, we can create **union key** to deal with high-frequence search.

    For exemple, we want get person name and its email, we can create a union key (name, email). One traversing can find both of them.

2. Leftest-Prefix-rule

    Since we've used **uinon key**. Whether there is a priority in it ?

    The answer is Yes. The leftest item in the uinon key is the first one used in the search.

    Even if you use **only the leftest** item in the uinon key in the query, this **union key can be used** to improve the performance. For exemple, if we search by `a`, we can use the index `(a, b)`.

    However, you want to search by `(a, b)` and `b`. Since `b` is not the leftest, you need to create another index. 

3. index condition pushdown

   For exemple, we have a table having a **union key**, (name, age). Here is the query

   ```sql
   select * from tuser where name like 'A%' and age=10 and ismale=1;
   ```

   Because of the leftest prefix rule, we can only use index `name`. If we need to re-traverse with the primary key for the rest ?

   The answer is no. **Index condition pushdown** will check the `age` before re-traversing because `age` is in the **key**.

   The same goes for:

   ```sql
    CREATE TABLE `geek` (
        `a` int(11) NOT NULL,
        `b` int(11) NOT NULL,
        `c` int(11) NOT NULL,
        `d` int(11) NOT NULL,
        PRIMARY KEY (`a`,`b`),
        KEY `c` (`c`),
        KEY `ca` (`c`,`a`), -- not needed
        KEY `cb` (`c`,`b`)
    ) ENGINE=InnoDB;
   ```

   `ca` is not needed. Because using the key `c` implies first using the index `c`, then using the primary key `a, b`. The `ca` is included in the `cab` thanks for **Index condition pushdown**. 

