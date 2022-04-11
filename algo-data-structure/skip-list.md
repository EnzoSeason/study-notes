# Skip list

Skip list is based on **linked list**.

It creates the **index** on the linked list. A common way is to **create 1 index node out of 2**.

For example, The orginal linked list has 8 nodes. We need create 2 index layers.

```
- 2nd index o - - - - - - - o
            |               |
- 1st index o - - - o - - - o - - - o
            |       |       |       |
- orignal   o - o - o - o - o - o - o - o
```

## Time complexity

What is the time complexity of finding a node in the skip list ?

We suppose the orginal linked list has `n` nodes. Since we create a index node out of 2, the `h` <sup>th</sup> layer has `n/2^h` nodes. So, the number of layer is `h = logn`

We suppose that we need traverse `m` nodes on each layer. So, we need to, in total, traverse `m*logn` nodes.

Again, Since we create a index node out of 2, `m` <= **3**.

- The last layer: `m` = 2

   There are only 2 nodes

- The rest layers: `m` = 3

    Suppose the node `i` is in the layer `k`. There is an formula.

    ```
    i->prev->val <= i->val <= i->next->val
    ```
The time complexity can be approached by the number of noded traversed. `m` is a constant. So the time complexity is `O(logn)`. It's very efficient.

For the other operation, like **inserting**, **deleteing**, the time complexity is `O(logn)`, too.

## Space complexity

How many nodes in the skip list.

As before, we suppose the orginal linked list has `n` nodes. The total nodes is calculated as followed.

```
s = 2 + 4 + 8 + ... + n/2^i + ... + n/4 + n/2 = n-2
```

The space complexity is `O(n)`.

## Update the indexes

To avoid turning a skip list into a list, we need to update the indexes dynamically.

When we **insert a item**, we can insert it into the indexes, too. We use a **random function** to decide the levels of indexes.

For example, if the random function returns `4`. We insert the item into `1, 2, 3, 4` <sup>th</sup> levels of indexes.





