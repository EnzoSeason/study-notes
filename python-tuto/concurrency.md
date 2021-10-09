#  Concurrency

# #  Concurrency vs Parallelism

- Concurrency: Only one task runs at a time. But, there are multiple tasks to run. OS decides when to run / stop a task.
   
   Python has 2 ways to do it:

   - asyncio
   - threading
    
       >Be careful about the **race condition**: multi threads share the same variable. They all can change it 

- Parallelism: run multiple tasks at the same time. They can be run on several machine or several cores. It's called multiple processes

Concurrency is for optimisation for I/O. We don't have to wait an I/O task finish to start another task. 

Parallelism is for CPU heavy situation. Add more machine to work. 

# #  asyncio

Asyncio in Python has **only one thread**. But, it uses **event loop** to do multiple tasks.

# #  GIL (Global Interpreter Lock)

While Python runs multiple threads. CPython, an interpreter of Python will run only one thread and block the others.

So, **Python can't run multiple threads if using CPython** as interpreter. It's because of GIL.

The reason using GIL:

- Most packages in C are not thread-safe, while CPython uses a lot of these packages.

- avoiding race condition

# #  Garbage Collection

To avoid **memory leak**, Python does garbage collection.

While a variable has **0 reference**, it will be collected, and memory will be released.

use `sys.getrefcount()` to get reference count.

```python
a = 1
print(sys.getrefcount(a)); #  2
```

**However**, Python will collect garage even though its reference is not 0.

```python
def func():
    a = [1]
    b = [2]
    a.append(b)
    b.append(a)

func()
```

It's **reference loop**. The reference of `a` or `b` will never be 0. This will cause **memory leak**.

Python can collect them automatically:

- mark-sweep: 

  traverse through all the variables, if a variable is not marked, sweep it.

  It costs too much. So, Python uses `generational` to optimise the process.

- generational:

  First init => first gen.

  After a cycle of garage collection and still alive => second gen

  Python has 3 gens.

  Each gen has a threhold. If the number of **init var** - that of **deleted var** > threhold, Python will do `mark-sweep` on this gen.

  So, the first gen is more likely to be collected.

Besides, we can visualize references' relationship using `objgraph`:

- `show_refs()`

- `show_backrefs()`

It helps us debug the **reference loop**.

We can call `gc.collect()` to collect garbage.
