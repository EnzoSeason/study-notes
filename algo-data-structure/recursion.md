# Recursion

A recursion has 2 key points.

- end condition

- recursion formula

End condition is the **edge case**.

Recursion formula presents the way of **spliting the problem into several sub problems**.

For example, [climbing stairs](https://leetcode.com/problems/climbing-stairs/). 

The edge cases are

- one staire
- two staires

The problem can be split to sum up the ways of climbing `n - 1` staires and `n - 2` staires.

So, the solution is simple.

```python
def climb_staires(n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    return climb_staires(n - 2) + climb_staires(n - 1)
```

What's more, we can use `Dynamic Programming`. It **caches the internal results** of the recursion.

```python
def climb_staires(n: int) -> int:
    dp = list(range(0, n+1)) # end condition: dp[1] = 1; dp[2] = 2
    
    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i - 2] + dp[i - 1] # recursion formula
    
    return dp[n]
```

## Stack overflow

A common problem of recursion is the **stack overflow**. 

We will create a space once a function is called. Then, we push this space into a stack. If the recursion is too deep, stack overflow happens.

## Repeated calculation

Somtimes, the same result can be calculated repeatedly.

For example, in climbing staires, we set `n == 4`:

```
- f(4)
  |-f(2)
  |-f(3)
    |-f(2)
    |-f(1)
```
`f(2)` is called 2 times.

We need to create a data structure to cache the internal results. `Dynamic Programming` uses an `array`.

Besides, we can use `hash map`.

```python
def climb_staires(n):
    hash_map = {}
    hash_map[1] = 1
    hash_map[2] = 2

    if n in hash_map:
        return hash_map[n]
    
    hash_map[n] = climb_staires(n - 2) + climb_staires(n - 1) 
    return hash_map[n]
```

