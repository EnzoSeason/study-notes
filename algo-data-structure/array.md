# Array

## Definition

1. Array is a **linear list**. 

2. Array uses a group of **contiguous memory space** to store a group of **data of the same type**.

## Linear List vs Non Linear List

Items in lineat list have **only two orientation**: forward and backward

Exemple: Array, Linked List, Stack, Queue

Those in Non Linear List have **multiply orientation**.

Exemple: Tree, Graph

## Advantage of Array

Because of using **contiguous memory space**, **visiting** items from array is very easy. We can use **index**.

Index (offset, to be more accurately) can get the address of array item in the memory.

```
array[i]_address = base_address + i * data_type_size
```

This formula also explains why we set the index of the first item in the array as 0.

## Disadvantage of Array

Because of using **contiguous memory space**, **inserting** and **removing** items are difficult. It needs modify almost entire array to keep contiguous.