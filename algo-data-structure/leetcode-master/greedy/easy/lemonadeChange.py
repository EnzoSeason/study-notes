from typing import List


class Solution:
    """
    https://leetcode.com/problems/lemonade-change/
    """

    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0] * 2

        for num in bills:
            if num == 5:
                cash[0] += 1
            if num == 10:
                if cash[0] > 0:
                    cash[0] -= 1
                    cash[1] += 1
                else:
                    return False
            if num == 20:
                #  greedy: use $10 first.
                if cash[0] > 0 and cash[1] > 0:
                    cash[0] -= 1
                    cash[1] -= 1
                elif cash[0] > 2:
                    cash[0] -= 3
                else:
                    return False
        return True