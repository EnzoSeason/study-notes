# Bitwise calculation

## Operators

- `&`: 有 0 出 0

- `|`: 有 1 出 1

- `^`: 相同出0， 不同出1

- `~`: 0->1 or 1->0

- `<<`: 左移 (*2)

- `>>`: 右移 (/2)

## `~` 

```python
x ^ 0 = x

x ^ 1s = ~x

x ^ (~x) = 1s

x ^ x = 0 # important

c = a ^ b => a = b ^ c or b = a ^ c # swap
```

## Practical use cases

1. odd or even (x % 2 == 0)

    ```
    x & 1 == 0
    ```

2. remove `1` in the lowest bit (very useful)

    ```
    x = x & (x-1)
    ```

3. get `1` in the lowest bit

    ```
    y = x & -x
    ```
    > -x = ~x + 1