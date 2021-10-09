#  BM (Boyer-Moore)

[Previously](./string-match-1.md), we've talked about BF & RF. Both of them have poor performance while find `aab` in `aaaaaaaaab`.

When a mismatch is occured, BF & RF will move the pattern by **one character**. That causes the poor performance.

To solve this problem, BM proposes 2 rules to follow.

- Bad Character Rule
- Good Suffix Rule

# #  Bad Character Rule

For exemple, we need to find `abd` in `abcababd`. The first **bad character** we meet is `c` in the main string.

```
abcababd
  |
abd
```

Instead of moving **one character**, we move the entire pattern to the next `a` (move **3 characters**).

```
abcababd
  |
   abd
```

Now, we meet another **bad character**, `a`. Unlike the last time, `a` is in the pattern. We should only move **2 characters**.

```
abcababd
     |
     abd
```

In general, Bad Character Rule defines a way to move pattern when the mismatch is met. We suppose that the index of the bad character in the pattern is `idx_bad`. If the conflicted main string's character is in the pattern, then we note this index as `idx_lastest_conflict`.

So, we should move:

```python
move = 1
if idx_lastest_conflict is not None:
    move = idx_bad - idx_lastest_conflict
else:
    move = idx_bad + 1
```

If we apply Bad Character Rule to find `aab` in `aaaaab`, we move **3 character** instead of **one**. It's a huge improvement.

# #  Good Suffix Rule

In the previous exemple, the bad character is the **last** character in the pattern. Let's a different case.

```
abbcbc
  ||
dbcbc
```

`bc` is the matched part in the dismatch. `bc` is **Good Suffix**.

If good suffix is in the pattern, we move the pattern to let them match.

```
abbcbc
  ||
 dbcbc
```

If not, we need to check if **prefix of pattern** matches **suffix of Good Suffix**. 

That also means to find the **longest prefix of pattern** match the **longest** part of **good suffix of pattern**

```
abcbc    abcbc
 ||    => ||
cbc        cbc
```

In this exemple, `c` is matched. We move **2 characters** instead of **3** (move the entire pattern back).


In general, there are 3 case:

1. The **good suffix** exists in the pattern

   move the pattern to let them match.

   *i.e.* `bc` is the good suffix. `abcdbc` is the pattern
   

2. The suffix of **good suffix** matches the **prefix** of pattern

   move the pattern to let matched part meet

   *i.e.* `abc` is the good suffix. `bcabc` is the pattern. `bc` is the matched part.

3. The other cases: no match

   move the entire pattern back.

# #  Bad Character Rule + Good Suffix Rule

BM combinds both of them.

```python
BM_move = max(bad_char_move, good_suffix_move)
```

