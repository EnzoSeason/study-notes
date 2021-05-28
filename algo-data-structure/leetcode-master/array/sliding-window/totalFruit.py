from typing import List


class Solution:
    """
    https://leetcode.com/problems/fruit-into-baskets/
    """

    def totalFruit(self, tree: List[int]) -> int:
        bag = {}
        left = 0

        for right in range(len(tree)):
            prod = tree[right]
            bag[prod] = bag.get(prod, 0) + 1

            if len(bag) > 2:
                prev_prod = tree[left]
                bag[prev_prod] -= 1

                if bag[prev_prod] == 0:
                    bag.pop(prev_prod)

                left += 1

        return right - left + 1