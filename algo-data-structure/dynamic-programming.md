# Dynamic Programming

## Why we need Dynamic Programming

When we use **Backtracking Algorithm** to solve the problems, such as [fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number), [Knapsack](https://en.wikipedia.org/wiki/Knapsack_problem), etc. The time complexity is `0(2^n)`. It's not efficient.

The cause of the high time complexity is the **internal results** are re-calculated, again and again.

Dynamic Programming can **cache** the internal states** so that it improves the time complexity.