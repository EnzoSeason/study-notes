## Log System

There are 2 important logs in MySql.

- **Redo log** in InnoDB engine
- **Binlog** in Server Layer

### Redo log

In MySql, there is a problem. If we want to update a piece of data. MySql needs to search the old data, find it and write the new one. The cost of IO is high.

To solve this problem, MySql uses a tech called **WAL** (Write-Ahead Logging). InnoDB engine will keep the update record in the **redo log** and wait. When it's not very busy, then it will write the data into database.

The size of redo log in InnoDB is fixed, 4GB. 

It uses **circular queue** as the data structure. The header is called `write_pos`, and the tail is `checkpoint`.

The cache in redo log won't be removed until redo log is full. The most accent data will be removed (**FIFO**). 

Because of redo log, InnoDB engine is **crash-safe**. It can recover the data by loading them from redo log when the database is crashed.

### Binlog

Like Redo log, Binlog also uses **WAL**. But, there are some difference.

- Binlog is in the **server layer**, while redo log is in **InnoDB**.

- Binlog logs the **raw logic** (sql or row's content). However, redo log records the operations on the InnoDB.

- The size of Binlog is **dynamic**. MySql will create a new file if the current file is full. But, redo log's size is fixed. Old records will be removed if the file is full.

Usually, if we want to recover a database or add the distributed database, we will **copy the entire database** + **using binlog**.

### Redo log + Binlog

For exemple, we need to update a field in a row in a table.

Before updating, we need find the old data. We, first, **check the memory**, if the data is data is not found, we **get the data from the disk**.

Then, we update the data. From now, redo log and binlog start to work.

1. The new data is set in the memory and InnoDB inserts a new record in **redo log** with **prepare** status. It tells the executor that the new data is ready for be inserting into disk.

2. The executor adds this record into **binlog**.

3. The executor executes the query. Then the InnoDB updates the record **from prepare to commit**.


Each record in redo log has 2 mode, `prepare` and `commit`. That makes sure the **consistency** when database changes (recover / inscrease the database).
