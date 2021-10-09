#  Complexity

# #  Time complexity

```math
T(n) = O(f(n))
```

- `n`: the size of the data

- `f(n)`: the number of codes run by CPU

- `O(f(n))`: the time needed for runing codes

Time complexity presents the relation between **the size of data** and **the time needed for running codes**, `T(n)`. So, it's usually written in `O(1)`, `O(n)`, `O(n^2)`, etc.

# # #  Analysis of Time complexity

There are 3 rules

1. check the loops

    ```python
    def func_1(n):
       a = 1

       for b in range(5):
           pass

       for c in range(n):
           pass
    ```

    `func_1` runs `2n + 11` lines of codes. So, `T(n) = O(n)`.

    > Notes: Although `range(5)` is a loop, the number of the codes is defined.

    ```python
    def func_2(n):
       a = 1

       for b in range(n):
           for c in range(n):
               pass
    ```
    `T(n)` of the `func_2` is `O(n^2)`.

2. addition

   ```
   IF : 
   T1(n)=O(f(n)); T2(n)=O(g(n))
   
   THEN: 
   T(n)=T1(n)+T2(n)
       =max(O(f(n)), O(g(n))) 
       =O(max(f(n), g(n)))
   ```
   In practice, we only look for the "biggest" loop.

    ```python
    def func(n):
       for a in range(n):
           pass

       for b in range(n):
           for c in range(n):
               pass
    ```
    `T(n)` of the `func` is `O(n^2)`.

3. multiplication


    ```
    IF : 
    T1(n)=O(f(n)); T2(n)=O(g(n))
    
    THEN: 
    T(n)=T1(n)*T2(n)
        =O(f(n)) * O(g(n)) 
        =O(f(n) * g(n))
    ```
    In practice, we looks for the **relation among the functions**.

    ```python
    def func_1(n):
        for a in range(n):
            for b in range(n):
                pass
    
    def func(n):
        for i in range(n):
            func_1(i)
    ```
    `func` calls `func_1`. So, we apply the rule of multiplication. `T(n)` = `O(n * n^2)` = `O(n^3)`


There are 2 kinds of Time complexity.

1. Deterministic Polynomial

    `O(1)`, `O(n^k)`, `O(logn)`, `O(nlogn)`, `O(m+n)`

    ```python
    #  O(logn)
    def func_1(n):
        i = 1
        while (i < n):
            i = i * 2

    #  O(nlogn)
    def fun(n):
        for i in range(n):
            func_1(1)   
    ```

    `O(m+n)` is created for 2 data input. Because we don't know the size of `m` and `n`, **the rule of addition** is failed, `max()` won't work.

2. Non-Deterministic Polynomial

    `O(2^n)` and `O(n!)`
    
    It's NP problem.

# #  Space complexity

Similar to Time complexity, Space complexity presents the relation between **the size of data** and **the space needed for running codes**.

For exemple, there is a function.

```python
def func(n):
    a = [i for i in range(n)]
```

Its space complexity is `O(n)`.

# #  Cases of Time complexity

There are 4 cases: 

- **best** case time complexity
- **worst** case time complexity
- **average** case time complexity
- **amortized** time complexity

Usually, we use the first three. 

To get Average `T(n)`, we need to calculate the probability of each case and return the weighted mean value.

Exemples:

```python
def find(arr: list, x: int) -> int:
    for i in arr:
        if i == x:
            return i
    return -1
```

- best: `O(1)`
- worst: `O(n)`
- average: 

    We assume the probability of find the `x` in `arr` is 50%, then the average Time complexity is:

    ```
    O(1/2n + 2/2n + 3/20 + ... + n/2n + n/2) = O(n)
    ```

```python
MAX_LEN = N #  N is a global const number

def insert(arr: list, val: int, pos: int) -> list:
    if pos >= MAX_LEN:
        sum_val = 0
        for i in arr:
            sum_val += i
        arr = [sum_val]
        arr.append(val)
        pos = 2
    else:
        arr[pos] = val
        pos += 1
    return [arr, pos]
```

- best: `O(1)`
- worst: `O(n)`
- average: 

    ```
    O(1/(n+1) + 1/(n+1) + 1/(n+1) + ... + 1/(n+1) +n/(n+1))
    ```

   