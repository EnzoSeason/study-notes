## Function

```python
def my_func(param1, param2, ..., paramN):
    statements 
    return/yield value ## optional
```

The function must be defined before using it.

- We don't have to define the type of params.

- We can write function inside a function (Nested function)

  This feature brings some advantages:
  
  1. keep the inside function private
  2. improve the efficiency

  More importantly, we can create `closure`. It's a function returns the inner function. 
  
  Inner function uses the environment provided by outer function.

    ```python
    def nth_power(exponent):
        def exponent_of(base):
            return base ** exponent
        return exponent_of

    square = nth_power(2) 
    cube = nth_power(3)

    print(square(3)) ## 9 square uses the env which has exponent == 2
    print(cube(5)) ## 125
    ```

### Default params

Default param always point to an immutable object

```python
def add_end(L=[]):
    L.append('END')
    return L

add_end() ## ['END']
add_end() ## ['END', 'END']
```

We can change the function.

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

### Changable params

We can use `*params` to represent multiple params of a function. Python passes these params into a `tuple` automatically.

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2, 3) ## 14

nums = [1, 2, 3]
calc(*nums) ## 14
```

### keyword params

We can use `**kw` to represent `k-v` params. Python passes them into `dict`.

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing') ## Bob age: 35 other: {'city': 'Beijing'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) ## name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

If we want to set limits on `key`, we can defind function:

```python
## function only takes city and job as the key of **kw

## * separate normal params from keyword params
def person(name, age, *, city, job):
    print(name, age, city, job)

## If function has changable params, we don't need *.
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

To put `normal params`, `default params`, `changable params`, `keyword params` all together.

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1, 2) ## a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3) ## a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b') ## a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
```

### Function variable scope

1. Variable created in the function only works in function

2. Function can use Global Variable, but it can't change it. If we want to change it, we must use keyword `global`.

    ```python
    MIN_VALUE = 1
    def validation_check(value):
        global MIN_VALUE
        ...
        MIN_VALUE += 1
    ```
3. If the local variable and global variable has the same name, function will use local variable.

4. If Nested function want to use the variable of outer function, it needs to use keyword `nonlocal`.

    ```python
    def outer(): 
        x = "local" 
        
        def inner(): 
            nonlocal x  
            x = 'nonlocal' 
            print("inner:", x) 
        
        inner() 
        print("outer:", x)
    
    outer()

    ## inner: nonlocal
    ## outer: nonlocal
    ```

### lambda function

```python
lambda argument1, argument2,... argumentN : expression
```

lambda function focus at tasks which are:

- simple

- use only once (or few times)

```python

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1]) ## sorted by the second element of each tuple
print(l)

## [(2, -1), (3, 0), (9, 10), (1, 20)]
```

There are some built-in function work with lambda function:

- `map(function, iterable)`:
    
    ```python
    l = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, l) ## [2， 4， 6， 8， 10]
    ```

- `filter(function, iterable)`:

    ```python
    l = [1, 2, 3, 4, 5]
    new_list = filter(lambda x: x % 2 == 0, l) ## [2, 4]
    ```

- `reduce(function, iterable)`:

    ```python
    l = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, l) ## 1*2*3*4*5 = 120
    ```