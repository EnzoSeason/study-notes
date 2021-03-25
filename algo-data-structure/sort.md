# Sort

There are a lot of sort algorithms. How can we choose a good one ? 

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

## O(n^2) sort

- Bubble Sort
- Insert Sort
- Selection Sort

### Bubble Sort

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

### Insert Sort

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

### Selection Sort

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








