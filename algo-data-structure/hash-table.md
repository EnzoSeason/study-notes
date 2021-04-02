# Hash Table

If we want to save the data for fast searching, we will use an array. However, we must use a non negative integer as an index. Can we custom the index ? Hash table is created for that.

Hash table is based on the **array**. It stocks **key-value** paires. **Hash function** transform the key into the index of the table.

## Hash function

The key point of the hash table is hash function, `hash()`. To make sure the index is well created, there are some rules to follow.

1. `hash(key)` is an integer and `hash(key) >= 0`.

2. If `k_1 == k_2`, then `hash(k_1) == hash(k_2)`

3. If `k_1 != k_2`, then `hash(k_1) != hash(k_2)`

The third rule is very strict. None of the [hash algorithms](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) can 100% make sure the third rule is applied.

If `k_1 != k_2`, `hash(k_1) == hash(k_2)`, then it's a **collision**.

There are 2 ways to solve the collision.

1. open addressing

2. chaining

### open addressing

The main idea of open addressing is if there is a collision, then we find another empty space.

The easiest implement is **linear probing**.

- When we **add** an item and meet the collision, we look for the next **empty** or **deleted-marked** space.

  > The array is circular.

- When we **delete** an item, we mark the space as **deleted**.

- When we **search** an item, if the item is not found, we will check the next item util meet the **empty** space.

As we can see, the time complexity of all 3 operation will approach `O(n)` with the growth of data. 

The more data is in the hash table, the more collisions we will meet, and the less efficient it becomes.

There is a factor to describe how full the hash table is, **load factor**.

```
load factor = the number of empty space / the length of the table
```


### chaining

Chaining is a more **common** and **simple** implement.

Instead of insert the value directly in the table, we put the **linked list** in it. We call it, **bucket** or **slot**.

A hash value maps a bucket. If we meet collision, we simply **add a new node** in the bucket.