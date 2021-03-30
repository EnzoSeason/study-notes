# Sort

There are a lot of sort algorithms. We classify them by time complexity.

- [`O(n^2)`](##O(n^2))

- [`O(nlogn)`](##O(nlogn))

- [`O(n)`](##O(n))

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

## O(n)

The sort whose time complexity is `O(n)` are called **linear sort**.

There are 3 common linear sorts.

- [bucket sort](###bucket_sort)
- [counting sort](###counting_sort)
- [radix sort](###radix_sort)

These 3 sorts are NOT based on the **comparaison**. That's the main reason that their time complexities are `O(n)`. 

However, these sorts have strict demande on **data format**.

### bucket_sort

We split the data into serveral **ordered bucket**. Then we do `O(nlogn)` sort, like quick sort, in each bucket.

The most tricky part in this sort is how to **create the buckets** that make **data split evenly in each bucket**.

#### Time complexity

If we have n items and `m` buckets, then in each bucket, we have `k = n/m` items. 

The time complexity of each bucket is:

```
O(klogk) = O(n/m * log(n/m))
```

The time complexity of bucket sort is:

```
m * O(n/m * log(n/m)) = O(n * log(n/m))
```

When `m` approaches `n`, the time complexity approach to `O(n)`.

#### Limits

- Buckets are ordered
- Data is even in each bucket.

  If the data isn't even, some buckets have a lot of data, some have little. The time complexity will become `O(nlogn)`.

#### usage

A use case is sorting the **huge external data**. 

We can't put all the data into the memory at once. So, we traverse all the data, find **the distribution of the data** and create the buckets. Then we sort bucket by bucket.

### counting_sort

The main idea of counting sort is to **count how many numbers** is smaller / bigger than **current** number.

Counting sort does 2 things:

1. create an array `C`. 

    The `C[i]` means there are `C[i]` items equal or small/bigger than `i`.

2. traverse the orignal array and sort it using the array `C`

The first part is composed by 2 steps.

1. bincount

    ```python
    C = np.bincount(arr)
    ```

2. accumulate
  
    ```python
    C = np.add.accumulate(C)
    ```

In this part, we can find the **limits** of counting sort.

1. The data in the array **must be positive**. Because the array `C` can't have a negative index.

2. The data in the array **can't be sparse**. If the data is sparse, we will have a lot of `0` in the `bincount` step, and the array `C` will be huge. It can be **much biggest** than the orignal array.

The second part is more tricky.

1. read the orignal array **from bottom to top**.

    The order is important. It makes counting sort **stable**. The position of the same value won't be changed after sort.

2. take the value of orignal array as an index of the array `C`, then take the value of array `C` as an index of sorted array, finally, fill in the value of orignal array

    ```python
    idx_c = org_arr[i]
    
    # C[idx_c] means the numbers of items whose value <= idx_c .
    # So we need to -1 to transform it into index of sorted array.
    idx_sorted_arr = C[idx_c] - 1 
    
    sorted_arr[idx_sorted_arr] = org_arr[i]
    
    # The numbers of items whose value <= idx_c reduces 1.
    C[idx_c] -= 1
    ```

The entire implement is as followed.

```python
from typing import List

def _accumulate_bincount(nums: List[int]) -> List[int]:
    len_acc_bincounts = max(nums) + 1
    acc_bincounts = [0 for _ in range(len_acc_bincounts)]

    # bincount
    for num in nums:
        acc_bincounts[num] += 1
    # accumulate
    for i in range(1, len_acc_bincounts):
        acc_bincounts[i] += acc_bincounts[i-1]
    
    return acc_bincounts

def _fill_sorted_nums(nums: List[int], acc_bincounts: List[int])-> List[int]:
    sorted_nums = [0 for _ in nums]
    i = len(nums) - 1

    while i >= 0:
        idx_acc_bincounts = nums[i]
        idx_sorted_nums = acc_bincounts[idx_acc_bincounts]
        sorted_nums[idx_sorted_nums - 1] = nums[i]

        acc_bincounts[idx_acc_bincounts] -= 1
        i -= 1
    
    return sorted_nums

def counting_sort(nums: List[int]) -> List[int]:
    acc_bincounts = _accumulate_bincount(nums)
    sorted_nums = _fill_sorted_nums(nums, acc_bincounts)

    return sorted_nums
```

### radix_sort

Radix sort must apply the rule, high position takes priority over low position.

For example, `20` > `18`. Although `8 > 0`, `2 > 1` so that `20 > 18`.

Radix sort sorts the radix **from low to high** using `O(n)` sort, such as bucket sort or counting sort.

