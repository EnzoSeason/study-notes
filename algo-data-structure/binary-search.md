#  Binary Search

If we want to find a number in a **ordered** data set, we can use binary search. 

we suppose the data is in the range from `min` to `max`. We, first, compare `mid` with the searched number, `num`.

- If `num` == `mid`, return True
- If `min` >= `max`, return False
- If `num` < `mid`, continue the search on the range [`min`: `mid`]
- If `num` > `mid`, continue the search on the range [`mid`: `max`]


There are some key points to read a correct binary search.

1. **End** condition

   The condition that returns True or False

2. Update `min` and `max`

   **When and How** to update `min` and `max` are important.


Here is 2 ways to implement binary search.

```python
def binary_search(nums: List[int], num: int) -> bool:
    my_nums = nums.copy()

    while len(my_nums) != 0:
        mid_idx = len(my_nums) // 2
        
        if num == my_nums[mid_idx]:
            return True
        if num < my_nums[mid_idx]:
            my_nums = my_nums[0:mid_idx]
        if num > my_nums[mid_idx]:
            my_nums = my_nums[mid_idx+1:len(my_nums)]
    
    return False

def binary_search_recursive(nums: List[int], num: int) -> bool:
    if len(nums) == 0:
        return False

    mid_idx = len(nums) // 2
    if num == nums[mid_idx]:
        return True
    if num < nums[mid_idx]:
        return binary_search_recursive(nums[0:mid_idx], num)
    if num > nums[mid_idx]:
        return binary_search_recursive(nums[mid_idx+1:len(nums)], num)
```

# #  Time complexity

We use the **times of comparaison** to approach the time complexity.

We suppose the length of the ordered array is `n`. After we compare `k` times, the array can't be split into 2. That also means the length of the array is `1`. We can have an equation.

```
n / 2^k = 1
```

So, `k = logn`

The time complexity is `O(logn)`.

`O(logn)` is very good to deal with large data set.

# #  Limits

1. The data must be **ordered**.

2. We must use **array** to stock data.
   
   Binary search needs the index. Linked list isn't suitable.

3. The size of data shouldn't be too big, neither too small.

    - too small: We just need traverse the data.
    - too big: We can put all the data int the memory.

# #  Typical use cases

Previously, we use biinary search to find the **equal** item. Here, we add some extra condition.

# # #  Find First Equal

This extra condition can be transformed as followed.

```python
if given_num == nums[mid_idx]:
    #  extra condition
    if mid_idx == 0 or nums[mid_idx-1] != given_num:
        return True
    else:
        #  not the first one, keep searching
        high_idx = mid_idx - 1
```

Full implement

```python
def first_equal(nums: List[int], given: int) -> int:
    low = 0
    high = len(nums)

    while low <= high:
        mid = low + (high - low) // 2
        if given > nums[mid]:
            low = mid + 1
        elif given < nums[mid]:
            high = mid - 1
        else:
            if mid == 0 or nums[mid-1] != given:
                return mid
            else:
                high = mid - 1

    return -1
```

# # #  First Equal or Greater

This extra condition can be transformed as followed.

```python
if nums[mid_idx-1] >= given_num:
    #  extra condition
    if mid_idx == 0 or nums[mid_idx-1] < given_num:
        return mid_idx
    else:
        high_idx = mid_idx - 1
```

Full implement

```python
def first_greater_equal(nums: List[int], given: int) -> int:
    low = 0
    high = len(nums)

    while low <= high:
        mid = low + (high - low) // 2
        if given <= nums[mid]:
            if mid == 0 or nums[mid-1] < given:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    
    return -1
```
