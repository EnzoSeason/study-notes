from typing import List


class Solution:
    """
    https://leetcode.com/problems/fruit-into-baskets/

    Best answer:
    https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements
    """

    def totalFruit(self, tree: List[int]) -> int:
        bag = {}
        max_len = 0

        l, r = 0, 0
        while r < len(tree):
            bag[tree[r]] = bag.get(tree[r], 0) + 1

            while len(bag) > 2:
                bag[tree[l]] -= 1
                if bag[tree[l]] == 0:
                    bag.pop(tree[l])
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len