from typing import List


class Solution:
    """
    https://leetcode.com/problems/counting-bits/submissions/
    """

    def countBits_method1(self, num: int) -> List[int]:
        """
        use hammingWeight in a loop
        """
        counts = [0 for _ in range(num + 1)]
        for i in range(num + 1):
            x = i
            while x:
                counts[i] += 1
                x &= x - 1
        return counts

    def countBits_method2(self, num: int) -> List[int]:
        """
        use DP

        Apply remove the lowest 1 on the index
        """
        counts = [0 for _ in range(num + 1)]

        for i in range(1, num + 1):
            counts[i] = counts[i & (i - 1)] + 1

        return counts