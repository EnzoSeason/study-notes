# Heap

Heap is a special tree.

- Heap is a **complete binary tree**.

- Every node must be smaller / bigger or equal to **all** the nodes in **its sub trees**.

## Data structure

Since the heap is a complete binary tree, the **array** is more suitable for storing data.

If the data of the node `i` is saved in `arr[i]`, then its left child is saved in `arr[2*i]`, its right child is in `arr[2*i + 1]` and its parent is in `arr[i // 2]`. 

> `arr[0]` is null.

## Operation

```python
class MinHeap:
    def __init__(n: int):
        self.arr = [None] # heap
        self.n = n # capacity
        self.count = 0 # current volume
```

### Insert

1. put the new data at the **end** of the array.

2. heapify: from bottom to top
    
    There are 2 types of heapifying.

    - from bottom to top
    - from top to bottom

    In the insert operation, we use the first one.

    ```python
    def heapify_bottom2top(self):
        '''
        from bottom to top heapify for a min-heap
        '''
        i = self.count
        while i // 2 != 0:
            if arr[i//2] > arr[i]:
                arr[i], arr[i//2] = arr[i//2], arr[i]
                i = i // 2
            else:
                break       
    ```
    Time complexity: `O(logn)`.

### Delete

1. remove the **first** item, `arr[1]`, in the array.
2. replace `arr[1]` by the **last** one, `arr[n-1]` (n = `len(arr)`).
3. heapify: from top to bottom

   ```python
    def heapify_top1bottom(self, top: int):
        '''
        from top to bottom heapify for a min-heap
        '''
        i = top
        while i <= self.n // 2:
            if arr[2*i] < arr[i]:
                arr[i], arr[2*i] = arr[2*i], arr[i]
                i = 2 * i
            elif arr[2*i+1] < arr[i]:
                arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
                i = 2 * i + 1
            else:
                break
   ```
   Time complexity: `O(logn)`.

### Create a heap

Since we have 2 ways to heapify, we have 2 ways to create a heap.

1. put the **first** item into `arr[1]` and keep **inserting** the new items into the heap.
   
   ```python
   def dummy_build(self, arr: List[int]):
        if len(arr) > self.n or len(arr) == 0:
            return
        self.arr = [0, arr.pop(0)]
        self.count = 1
        for data in arr:
            self.insert(data)
            self.count += 1
   ```

   Time complexity: `O(nlogn)`.
   
   The time complexity can be approach by **the times of inserting**. The function `insert` is `O(logn)` and it is called `n` times.

2. from the **last non-leaf node**, `arr[n//2]`, to the top, heapify it.

    ```python
    def build(self, arr: List[int]):
        if len(arr) > self.n:
            return
        self.arr = [0] + arr
        self.count = len(n)
        i = self.count // 2
        while i != 0:
            self.heapify_top2bottom(i)
            i = i // 2
    ```

    Time complexity: `O(n)`
    
    The time complexity can be approach by **the times of heapifying**. We heapify **all** the sub-tree, inclue the entire tree. So the times of heapifying is, 

    S =  &sum;2<sup>h-i</sup> * (h-i) *(1 <= i <= h)*

    To calculate it:

    S = 2S - S = &sum;2<sup>i</sup> - h *(1 <= i <= h)*
    
    Now, we have 2 equation.
    
    - S = 2<sup>h+1</sup> - 2 + h
    - h = logn

    S = `O(n)`. So the time complexity is `O(n)`.

### Sort

After the min-heap is built, the top, `arr[1]`, is the smallest item. The sort is to swap `arr[1]` with `arr[n]` and heapify `arr[1:n]`.

The result is:

- min-heap => desc array
- max-heap => asc array

```python
def sort(self, arr: List[int]):
    self.build(arr)

    i = self.count 
    while i != 0:
        sorted_arr[1], sorted_arr[i] = sorted_arr[i], sorted_arr[1]
        self.heapify_top1bottom(1)
        i -= 1
    
    return sorted_arr
```
The time complexity is `O(nlogn)`. It isn't stable because of heapifying. It's sort in place, the space complexity is `O(1)`.

The heap sort is **not by the order of the index**. It's not friendly for CPU. Beside, **the times of switch** is too much during **heapifying**. That's why people usually choose **Quick sort** than **Heap sort**.





