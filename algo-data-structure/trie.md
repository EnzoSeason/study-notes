# Trie

Trie is a **tree** to save the **strings**. It's used in the **search engine**. It's efficient to **find words by given prefix**.

The node of Trie saves only **one character**. The **path** represents a word.

For example, `cat` and `cow` are saved in a Trie.

```
            |- a - t
<root> - c -|
            |- o - w
```

A node, usually, has 26 children which represent 26 children.

```python
# 26 alphabets
NODE_SIZE = 26

class TrieNode:
    def __init__(self):
        # Children contains TrieNodes.
        # The index of children represents the character.
        # For example, 0 => a
        self.children = [None] * NODE_SIZE
        self.isEndOfWord = False
```

## Operations

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Suppose that word ONLY contains 26 alphabets
        """
        p = self.root
        word = word.lower()

        for c in word:
            idx = ord(c) - ord("a")
            if p.children[idx] is None:
                p.children[idx] = TriNode()
            p = p.children[idx]

        p.isEndOfWord = True

    def isFind(self, pattern: str) -> boolean:
        """
        Suppose that pattern ONLY contains 26 alphabets
        """
        p = self.root
        pattern = pattern.lower()

        for c in pattern:
            idx = ord(c) - ord("a")
            if p.children[idx] is None:
                return False
            p = p.children[idx]

        if not p.isEndOfWord:
            return False

        return True
```

Both `insert` and `isFind` is `O(n)` (`n` is the length of the input string). It's very efficient.

## Example

[Leetcode 208](https://leetcode.com/problems/implement-trie-prefix-tree/)
