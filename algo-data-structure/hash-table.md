## Hash Table

If we want to save the data for fast searching, we will use an array. However, we must use a non negative integer as an index. Can we custom the index ? Hash table is created for that.

Hash table is based on the **array**. It stocks **key-value** paires. **Hash function** transform the key into the index of the table.

### Hash function

The key point of the hash table is hash function, `hash()`. To make sure the index is well created, there are some rules to follow.

1. `hash(key)` is an integer and `hash(key) >= 0`.

2. If `k_1 == k_2`, then `hash(k_1) == hash(k_2)`

3. If `k_1 != k_2`, then `hash(k_1) != hash(k_2)`

The third rule is very strict. None of the [hash algorithms](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) can 100% make sure the third rule is applied.

A good hash algorithm must has following features.

1. We can't get **orginal data** from **hash value**.

2. The probability of collision must be very small. **Different data has different hash value**.

3. Similar data has very different hash value.

4. The calculation of hash value is fast.

The first and second feature are very important. Because of these features, hash function is always used to **create IDs**.

If `k_1 != k_2`, `hash(k_1) == hash(k_2)`, then it's a **collision**.

There are 2 ways to solve the collision.

1. open addressing

2. chaining

#### open addressing

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

When the **load factor** is too big, we need to inscrease the space of the hash table. 

A proper way to do is, first, create a empty array but do not move the date from the old one. When we insert / delete an item, we move an item from the old array to the new one. 

To sum up:

- Advantage: 

  - It's fast to find an item
  
- Disadvantage: 
   
  - It's difficult to insert / delete an item

  - When the load factor is too big, the performance is dropped dramatically.

  - It isn't easy to increase the capacity.

If the **data size is small**, It's good to use it.

#### chaining

Chaining is a more **common** and **simple** implement.

Instead of insert the value directly in the table, we put the **linked list** in it. We call it, **bucket** or **slot**.

A hash value maps a bucket. If we meet collision, we simply **add a new node** in the bucket.

To sum up:

- Avantage:

  - It's easy to insert / delete data.
  - It inscreases the capacity automatically.

- Disavantage:

  - It cost the extra space to stock the pointers.

  - It isn't as fast as *open addressing* to find an item.

If the **data size is big**, we choose chaining.

### Linked Hash Map

It's a common data structure in Java. It can:

1. find an item by `key` using **hash table**
2. insert / delete an item using **linked list**
3. If the max capacity is reached, the least recently used (LRU) item is removed.

As we can see, all the operation is `O(1)`. It's very efficient.

To understand Linked Hash Map, we can see it on 2 axes.

- axe x: a **hash table**. The value of it is an **one-way linked list**. This linked list is created for dealing with the collision (chaining).

- axe y: a **two-way linked list** to stock the key and the value.

The full implement is [here](https://github.com/EnzoSeason/study-notes/blob/main/algo-data-structure/hash-table/linked-hash-map.py)
