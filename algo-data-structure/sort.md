# Sort

There are a lot of sort algorithms. We classify them by time complexity.

- [`O(n^2)`](##O(n^2))

- [`O(nlogn)`](##O(nlogn))

## How to analyze a sort algorithm

There are 3 apects.

- Efficiency

  Some indicators are important to measure the efficiency 
  1. The best, worse and average **Time Complexity**.
  2. The **coefficient, constant, order** of `n`.
  3. The **times of comparasion and switch**.

- Memory consumption
  
  The **space complexity** should be considered.
  
  **Sorted in place** is a kind of sort whose space complexity is `O(1)`.
  
- Stability

  When there are **2 same items** in the list, if they haven't changed **relative position**, then the sort is **stable**.

  It depends on the implement. Change the list ONLY we need to.

## O(n^2)

- [Bubble Sort](###Bubble_Sort)
- [Insert Sort](###Insert_Sort)
- [Selection Sort](###Selection_Sort)

### Bubble_Sort

Bubble sort only operate on **two adjacent data**. If these 2 data **meet the switch condition**, we switch them.

```python
def bubble_sort(a: list) -> list:
  l = a.copy()
  n = len(l)

  if len(l) <= 1: return l
  
  for i in range(n):
    is_switched = False
    
    for j in range(n-i-1):
      if l[j] > l[j+1]: # switch condition
        l[j], l[j+1] = l[j+1], l[j]
        is_switched = True
    
    if is_switched == False: break

  return l
```

- Memory consumption
  
  It's sorted in place. `O(1)`

- Stability 
  
  Yes

- Efficiency

  - Best: Outter loop runs only one time. `O(n)`
  - Worse: `O(n^2)`
  - Average: difficult to calculate :( , but it's `O(n^2)`

We use **average switch times** to approach average time complexity.

For switch times:

- best
  
  No switch => `0`

  > In the case, all the pairs in the list are **ordered pairs**.

- worse
  
  switch every times => `n*(n-1)/2`

  > In the case, there is no **ordered pairs**.

So the average switch times is `( 0 + n*(n-1)/2 ) / 2`. The average time complexity approach is `O(n^2)`.

Here, we introduce a definition, *ordered pairs*.

```
# i < j is a sufficient not necessary condition

a[i] <= a[j], if i < j
```

*Reversed pairs* are the opposite of *ordered pairs*.

```
# i <= j is a sufficient not necessary condition

a[i] > a[j], if i < j
```

### Insert_Sort

The main idea is to insert a item into a **sorted list**.

So, we need to seperate a list into two parts, **sorted** and **unsorted**. We pick item from unsorted part and insert it into sorted part.

```python
def insert_sort(a: list) -> list:
  l = a.copy()
  n = len(l)

  if n <= 1: return l
  
  for i in range(1, n):
    val = l[i]
    j = i - 1
    # move sorted list
    while j >= 0:
      if l[j] > val: # switch condition
        l[j+1] = l[j]
        j -= 1
      else:
        break
    # insert
    l[j+1] = val
  return l
```

- Memory consumption
  
  It's sorted in place. `O(1)`

- Stability 
  
  Yes

- Efficiency

  - Best: Inner loop runs only one time. `O(n)`
  - Worse: `O(n^2)`
  - Average: use the times of switch to approach, `O(n^2)`

The times of the switch is **the number of the reversed pairs**.

### Selection_Sort

It also splits the list into **sorted** and **unsorted** parts. However, it selects the **minimal value** in the unsorted part and puts it at the **end** of the sorted part.

```python
def selection_sort(a: list) -> list:
  l = a.copy()
  n = len(l)

  if n <= 1: return l

  for i in range(n):
    for j in range(i, n):
      if l[i] > l[j]: # switch condition
        l[i], l[j] = l[j], l[i]
  return l 
```

- Memory consumption
  
  It's sorted in place. `O(1)`

- Stability 
  
  Yes

- Efficiency
  
  It needs to compare all the paires.

  - Best: `O(n^2)`
  - Worse: `O(n^2)`
  - Average: `O(n^2)`

## O(nlogn)

The main idea of `O(nlogn)` sort is **spliting a big array into small arrays**, then solving the small arrays.

- [Merge Sort](###Merge_sort)

- [Quick Sort](###Quick_sort)


### Merge_sort

The idea is simple.

1. split a big array into 2 arrays

3. merge 2 arrays into one by the order ASC / DESC. 

To make it simple, we split an array in 2.

```python
def _merge_sort_worker(arr: List[int], start: int, end: int) -> None:
    '''
    merge sort the arr[start:end] recursively
    '''
    
    # end-1 is the index of the last item is the array
    if start >= end - 1: 
        return
    
    mid = start + (end - start) // 2
    
    _merge_sort_worker(arr, start, mid)
    _merge_sort_worker(arr, mid, end)
    
    _merge(arr, start, mid, end)
```

In this example, we sort the array in asc.

```python
def _merge(arr: List[int], start: int, mid: int, end: int):
    '''
    merge arr[start:mid] and arr[mid:end]
    
    merged array is sorted.
    '''
    i = start
    j = mid
    merged_arr = []

    while i != mid and j != end:
        if arr[i] > arr[j]:
            merged_arr.append(arr[j])
            j += 1
        else:
            merged_arr.append(arr[i])
            i += 1
    
    if i != mid: merged_arr.extend(arr[i:mid])
    if j != end: merged_arr.extend(arr[j:end])

    arr[start:end] = merged_arr
```

Finally, we use merge sort.

```python
def merge_sort(arr: List[int]) -> List[int]:
    copied_arr = arr.copy()
    n = len(copied_arr)

    _merge_sort_worker(copied_arr, 0, n)
    return copied_arr
```

- Memory consumption
  
  It's sorted in place. `O(1)`

- Stability 
  
  Yes

- Efficiency

  - best: `O(nlogn)`
  - worst: `O(nlogn)`
  - average: `O(nlogn)`

#### How we get the `O(nlogn)` time complexity

In `merge sort`, we split an array into 2. So, if the time of sorting an array having `n` items is `T(n)`, then: 

```
# C is a constant.

T(1) = C

T(n) = 2*T(n/2) + n
T(n) = 2*(2*T(n/4) + n/2) + n = 4*T(n/4) + 2*n
...
T(n) = 2^k * T(n/2^k) + k*n
```

When n/2<sup>k</sup> == 1, so that **k = log<sub>2</sub>n**. 

We can get an equation about `n`.

```
T(n) = C*n + n*logn
```

Since `nlogn` is much larger than `n` when `n` approaches infinity. So, we get `O(n) = nlogn`.

### Quick_sort

The idea is:

1. choose a **random number** in the array as **pivot**.

2. put the the numbers that are smaller than the pivot before the pivot, the rest after the pivot. 

    > The array is split into 2 arrays.

3. do the step 1 & 2 on the arrays that are before & after the pivot

```python
def _quick_sort_worker(arr: List[int], start: int, end: int) -> None:
    if start >= end - 1: 
        return
    
    pivot_idx = _partition(arr, start, end)
    _quick_sort_worker(arr, start, pivot_idx)
    _quick_sort_worker(arr, pivot_idx+1, end)
```

```python
def _partition(arr: List[int], start: int, end: int) -> int:
    '''
    Tricky method:

    1. choose a random item in the array, and put it at the first / last position
    2. traverse the rest of array
    '''
    k = random.randint(start, end - 1)
    arr[k], arr[end - 1] = arr[end - 1], arr[k]
    pivot_idx = start

    for i in range(start, end - 1):
        if arr[i] < arr[end - 1]:
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
            pivot_idx += 1
        
    arr[end - 1], arr[pivot_idx] = arr[pivot_idx], arr[end - 1]
    
    return pivot_idx
```

> `_partition` is tricky. See [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) to learn more

- Memory consumption
  
  `O(1)`. It needs a temporaire memory to stock the array in `_merge` function.

- Stability 
  
  No. `_partition` change the positions of items having the same value.

- Efficiency

  - best: `O(nlogn)`
  - worst: `O(n^2)`
  - average: `O(nlogn)`

  The time complexity depends on the choice of **pivot**.

  For exemple, we always choose the last item as pivot of the array `[1, 2, 3, 4, 5]`. The time complexity is `O(n^2)`.

  That's why we choose a **random** item as a **pivot**.



