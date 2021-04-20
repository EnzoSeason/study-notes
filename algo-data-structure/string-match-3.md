# KMP

KMP is similar to BM. 

It uses the concepts of **bad character** and **good suffix**. 

It pays more attention on **pattern**. It studies **pattern** to decide how to move when mismatch is met.

KMP pre-process the pattern. It stocks the result of the "study" in an array, called PTM (Partial Match Table).

## Algo

When we meet **bad character**, we take **all the pattern before bad character** out as `arr`. 

We need to find the **longest** match between `arr`'s prefix and suffix, which is the "study" metioned previously.

For exemple,

```
main:    a b a b a b a b c a
                     |
pattern: a b a b a b c a
```
The mismatch is found, let's move the pattern.

```
main:    a b a b a b a b c a
                     |
pattern: > > a b a b a b c a
```

We move 2 characters and find the match. The question is how we know we should move 2 characters.

## PTM (Partial Match Table)

The array stored the "study" result is call PTM (Partial Match Table). `PTM[i]` means the **length** of the matched string.

```
pattern : a b a b a b c a
PTM     : 0 0 1 2 3 4 0 1
```

Explanation:

- `PTM[0] = 0`

   No **prefix** to match

- `PTM[1] = 0`

   In the string `ab`, the last `b` doesn't matche the first `a`. So the matched string length is `0`.

- `PTM[2] = 1`

    In the string `aba`, the last `a` matches the first `a`. So the matched string length is `1`.

- `PTM[3] = 2`

    In the string `abab`, the last `ab` matches the last `ab`. the matched string length is `2`.

- ... (same to the `PTM[3] = 2`)

- `PTM[7] = 0`

   In the string `abababc`, the last `c` doesn't matche the first `a`. So the matched string length is `0`.

- `PTM[8] = 1`

    In the string `abababca`, the last `a` matches the first `a`, and `ca` doesn't matches the first `ab`. So the matched string length is `1`.

Back to the question, *how we know we should move 2 characters*. Since `c == pattern[7]`, we should check `PTM[0:7]`. `PTM[6]` tells us the **length** of the matched string is `4`, so we need to move `(7-1) - 4 = 2` characters. `7-1` means the length of the pattern before `c` (`ababab`).

In conclusion, if `pattern[i]` is the bad character, we need to check `PTM[i-1]` the **length** of the matched string. Finally, the number of moving character is `i - PTM[i-1] + 1`.

Now, we move **one** space in `PTM` and create the new array, `next`. It makes **the generation** of the `PTM` and **usage** of `PTM` simpler. It's tricky.

```
pattern :  a b a b a b c a
PTM     :  0 0 1 2 3 4 0 1
next    : -1 0 0 1 2 3 4 0 1
```

### Usage of PTM

KMP is the usage of `PTM`.

Suppose `PTM` is created, we use `next` array in the codes.

```python
def kmp(main: str, pattern: str) -> int:
    n = len(main)
    m = len(pattern)
    next_arr = generate_next_from_PTM(pattern)

    i = 0
    j = 0
    while i < n and j < m:
        if j == -1 or main[i] == pattern[j]:
            # check the next character in the main string
            i += 1
            j += 1
        else:
            # Thanks to moving one space back in PTM
            # If pattern[j] is the bad character, (main[i] != pattern[j])
            # We check next_arr[j] instead of PTM[j-1], which are the same.
            j = next_arr[j]
    
    if j == m:
        return i - j
    else:
        return -1
```

### Generation of PTM

```python
def generate_next_from_PTM(pattern: str) -> List[int]:
    m = len(pattern)
    next_arr = [-1 for _ in range(m+1)]

    i = 0
    j = -1
    while i < m:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next_arr[i] = j
        else:
            # key point
            j = next_arr[j]
    
    return next_arr
```


