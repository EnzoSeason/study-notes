#  Advance

# #  generator

Generator doesn't use RAM to save data util the program runs. It saves the storage of RAM.

There are two ways to create a generator:

- `(x for x in range(10))`:

   It looks like a list, but it uses `()` instead of `[]`.

- `yield`:

   In function, we use `yield` instead of `return` to create a generator. Different from `return`, `yield` just breaks the function, it doesn't exit the function
   
    ```python
    def odd():
        yield 1
        yield 3
        yield 5
    
    next(odd) #  1
    next(odd) #  3
    next(odd) #  5
    next(odd) #  error StopIteration
    ```

    Sometimes, to avoid having `StopIteration` error, we put `yield` in an infinit loop `while True`.


To use a generator, we use `next()`:

```python
g = (x for x in range(10))

next(g) #  0
next(g) #  1
next(g) #  2
```

# #  Iterable vs Iterator

- Iterable: the data structure that can be used in `for` loop

    `list, tuple, dict, set, str` and `generator`

- Iterator: the data structure that can be called by `next()`

    `generator`

To transform `Iterable` to `Iterator`, we use `iter()`

```python
from collections.abc import Iterable, Iterator
isinstance([], Iterable) #  True
isinstance([], Iterator) #  False
isinstance(iter([]), Iterator) #  True
```

# #  '==' vs 'is'

- '==': compare if the **value** is the same

- 'is': compare if the id is the same (pointer to the same address)

    ```python
    a = 10
    b = 10
    a == b #  True
    
    id(a) #  4427562448
    id(b) #  4427562448
    a is b #  True
    ```
    Python save the int, from -5 to 256, in a list.
    ```python
    a = 257
    b = 257
    a == b #  True
    
    id(a) #  4473417552
    id(b) #  4473417584
    a is b #  True
    ```
A common usage of `is` is compare if the variable is `None`:

```python
a = 10
if a is None:
    pass
```

# #  Shallow copy vs Deep copy

- Shallow copy: create a new RAM for the new variable, the elements in the new variable is the **reference** of these in the orignal variable.

> Attention: If the element in orignal variable is NOT **immutable**, the change of this element will be appled on the copy variable. Because they point at the same RAM.

```python
l1 = [[1, 2], 'a']
l2 = l1[:]

l1.append('b')
l1 #  [[1, 2], 'a', 'b']
l2 #  [[1, 2], 'a']

l1[0].append(3)
l1 #  [[1, 2, 3], 'a', 'b']
l2 #  [[1, 2, 3], 'a', 'b']
```

- Deep copy: the variable variable has **NO relationship** with the orignal one.

> Attention: Since deep copy use recursion to copy entire variable, it should avoid infinit loop.

use `deepcopy()` of `copy` package to de deep copy.

# #  Assignment

Example 1:

```python
a = 1
b = a
a += 1
```

> Remember, `int`, `str` are immutable in Python.

It does several things:

1. create a RAM for `1`, and let `a` point to it
2. create `b` as a new **reference** of `1`. Now, `a` and `b` point at the same RAM.
3. create a RAM for `2` and let `a` point to it. Now, `a` and `b` point to the different RAM.

Example 2:

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)

l1 #  [1, 2, 3, 4]
l2 #  [1, 2, 3, 4]
```

`l1` and `l2` point at the same RAM so that the change of `l1` happens on `l2`, too.

It's important to understand the difference between:

- create a new RAM
- edit on current RAM

# # #  function args

In Python, there isn't function args by value or by reference. It always **create an new reference**.

```python
def my_func1(b):
  b = 2

a = 1
my_func1(a)
a #  1
```
As *Example 1*, `b`, first, points at the RAM of `1`, same as `a`. Then it points at the new RAM of `1`. So that, `a == 1` 

```python
def my_func2(l2):
  l2.append(4)

l1 = [1, 2, 3]
my_func2(l1)
l1 #  [1, 2, 3, 4]
```

As *Example 2*, `l1` and `l2` always point at the same RAM.

The best pratice is:

- create new RAM for args
- return value

That ensures function doesn't accidentially change orignal data.

```python
def my_func2_plus(l2):
    l2 += [4]
    return l2

l1 = [1, 2, 3]
l1 = my_func2_plus(l1)
l1 #  [1, 2, 3, 4]
```

# #  Decorator

Decorator is a **closure**, a function return a function object.

```python
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper
```

```python
def greet():
    print('Hi')
greet = my_decorator(greet)
greet()

# # #  output # # # 
#  wrapper of decorator
#  Hi
```

Decorators is to modify the behavior of the function through a wrapper so we don’t have to actually modify the function.

```python
@my_decorator
def greet():
    print('Hi')

greet()

# # #  output # # # 
#  wrapper of decorator
#  Hi
```

Usually, we use `*args` and `**kw` pass params in decorator

```python
def my_decorator(func):
    def wrapper(*args, **kw):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper
```

We can pass paramas to decorator, too.

We just need to wrap the decorator.

```python

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)

greet('hello world')
```

# # #  class decorator

We can use class to create a decortaor, too.

We pass a function as an attr of class, `__call__` is the wrapper.

```python

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('wrapper of decorator')
        return self.func(*args, **kwargs)

@MyDecorator
def example():
    print("Hi")

example()

# # #  output # # # 
#  wrapper of decorator
#  Hi
```

# # #  multi decorator

Python allows to use multiple decorator.

```python
@decorator1
@decorator2
@decorator3
def func():
    pass
```

which is equal to

```python
decorator1(decorator2(decorator3(func)))
```

Decorators are executed **from top to bottom**.
# # #  example

Usually, decorators are used in **validation**, **authentication**, **log**, etc.

```python
import functools

def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        pass
    
@validation_check
def neural_network_training(param1, param2, ...):
    pass
```

>`@functools.wraps(func)` keeps the meta data of wrapped function.
