# Transaction Isolation

In gerneral, executing a sql query is a transaction.
 
Speaking of the transaction, ACID (Atomicit, Consistenc, Isolation, Durability) must come to our mind. This article will talk about **Isolation**.

There are 4 levels of isolation in the transaction.

1. **read uncommitted**: The change caused by the current transaction can be seen by other transactions **before the current transaction is committed**.

2. **read committed**: The change caused by the current transaction can be seen by other transactions **after the current transaction is committed**.

3. **repeatable read**: In a transaction, the **queried data** must **always be the same**.

4. **serializable**: When a transaction is reading or writing, all the other transaction is **locked**.

From level `1` to `4`, the isolation becomes better and better. However, the efficiency turns worse and worse.

## Implement

How do we implement the isolation ? We use the **rollback log**.

When we update the data, we will record all the **rollbacks** for different levels of isolation.

That's the reason that we should NOT write long transactions. Because these transactions need visit a lot of data in the database. That creates huge amounts of rollbacks.

Rollbacks is deleted when it's not needed, by MySql. 

