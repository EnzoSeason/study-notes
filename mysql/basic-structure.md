#  Basic Structure

MySql contains 2 layers.

- Server Layer
- Storage Engine Layer

Multi storage engines can share one server layer.

# #  Server Layer

**Most of core function** is in the server layer, including connectors, analyzers, optimizers, executors, etc.

# # #  Connector

Connector makes the connection between user and database.

```bash
mysql -h$ip -P$port -u$user -p
```

The connection is complicate. It's better to establish **long connection**. However, long connection costs the memory. MySql will **reset the connection** after a big operation is executed. It helps release the memory. (MySql > 5.7)

# # #  Analyzer

After the connection establised, MySql starts to execute the query. 

Firstly, it analyzes the query. It finds the **keywords**, such as, `SELECT`, `IN`, `WHERE`, etc. 

Then it **parses the query**. If it fails, MySql will return an **syntax error**.

# # #  Optimizer

Since MySql understands the query, it will execute it. But before that, it optimize the query first. It will decide **choose which index to use**. Sometime, Different choices of indexes have huge influence in the performance.

```bash
mysql> select * from t1 join t2 using(ID) where t1.c=10 and t2.d=20;
```

# # #  Executor

One last step before running the query is the role check. Role check can be place **before the executor** or **before the optimizer**.

If the check is failed, it will return `command denied`.

```bash
mysql> select * from T where ID=10;
```

Finally, MySql executes the query. It will use the **interfaces** given by the **storage engine**.

The search is started at **the first line** of a table. If the line matches the query, this line will be saved in the **result set**. Then, MySql scans the next line. In the end, MySql returns the entire result set.


# #  Storage Engine ayer

Storage Engine is responsible for **saving and getting** data. The default engine is **InnoDB**. There are other engine, such as **memory**.

