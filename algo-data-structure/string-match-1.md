## BF & RF

BF (Brute Force) and RF (Rabin-Karp) are two methods of **string match**.

### BF (Brute Force)

It's the easiest way for string. It compares the **pattern** with the **main string** character by character.

```python
def bf(main_str: str, pattern: str) -> int:
    n = len(main_str)
    m = len(pattern)
    
    for idx_main in range(n - m + 1):
        count = 0
        
        for idx_sub in range(m):
            if pattern[idx_sub].lower() != main_str[idx_main+idx_sub].lower():
                break
            count += 1
        
        if count == m:
            return idx_main
    
    return -1
```

The worse case is we compared `(n*m+1) * m` times. The time complexity is `O(n*m)`.

BF isn't good at deal with special cases, such as finding `ab` in `aaaaaaaaab`. However, this type of cases is rare at work. BF is widely used because of its simplicity.

### RF (Rabin-Karp)

RF is similar to BF. The main difference is that it compares **hash value** of the string instead of itself.

To create a hash function, we need to consider 2 processes.

1. Map [a, z] to **numbers**. *i.e 'abc' => '123'* 
2. Transform numbers to **value**. *i.e 'abc' => '123' => 1\*26^2 + 2\*26 + 3*

There are a lot of hash function. We present one of them.

```python
def hash(val: str) -> int:
    """
    1. Map a-z into their acsii value 
    2. Tranform the value to reversed decimal
    """
    res = 0
    pos = 0
    for i in range(len(val)):
        c = val[i].lower()
        res += ord(c) * (26**pos)
        pos += 1
    return res
```

Now, the time complexity is `O(n)`.

```python
def rf(main_str: str, pattern: str) -> int:
    n = len(main_str)
    m = len(pattern)
    pattern_hash = hash(pattern)
    
    for idx_main in range(n - m + 1):
        sub_str = main_str[idx_main: idx_main + m]
        sub_hash = hash(sub_str)
        
        if sub_hash == pattern_hash and compare(sub_str, pattern):
            return idx_main
    
    return -1
```

#### Limits

1. large pattern
  
    It can't deal with **large pattern**. The hash value will be too big to be memorized.

    To solve this problem, we need to **split the pattern into serval parts**, and match them one by one. However, the time complexity is `O(n*p)` (p is the number of the parts) instead of `O(n)`. It makes **RF** approach **BF**. 

2. hash collision

   We **compare 2 strings** when we meet hash collision.

    ```python
    def compare(main_str: str, sub_str: str) -> bool:
        n = len(main_str)
        m = len(sub_str)

        if n != m:
            return False

        for i in range(n):
            if main_str[i] != sub_str[i]:
                return False

        return True
    ```

