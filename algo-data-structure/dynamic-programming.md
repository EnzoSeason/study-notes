#  Dynamic Programming

# #  Why we need Dynamic Programming

When we use **Backtracking Algorithm** to solve the problems, such as [fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number), [Knapsack](https://en.wikipedia.org/wiki/Knapsack_problem), etc. The time complexity is `0(2^n)`. It's not efficient.

The cause of the high time complexity is the **internal results** are re-calculated, again and again.

Dynamic Programming can **cache the internal states** so that it improves the time complexity.

# #  Theory

Dynamic Programming has "one model" and "three features".

# # #  Model

We use dynamic programming to solve **optimal problems**.

The process of solving problems requires multiple decision-making stages. Each **decision stage** corresponds to **a set of states**. We use **the states** to solve optimal problems.

# # #  Feature 1: Optimal substructure

Solving a **optimal problem** can be splited by solving multiple **optimal sub-problems**.

That means the state of the **later stage** can be derived from the state of the **previous stage**.

# # #  Feature 2: No aftereffect

- We only care about **the state value of the previous stage**, not how this state is derived step by step.

- Once the state of a **certain stage** is determined, it will **NOT be affected** by the decision of the **subsequent stage**.

# # #  Feature 3: Duplicate sub-problems

The states of stage can be duplicated because of recursion. That's why we need to cache the states.

# #  Solving DP

There are 2 ways.

1. solving it from **start** stage to **end** stage.

2. solving it from **end** stage to **start** stage.

   It's recommended way. We need to write the **State Transition Equation**.

   ```
   #  init
   f[0] = a, f[1] = b, ...
   
   #  State Transition Equation
   f[n] = g(f[n-1], f[n-2], ... )
   ```