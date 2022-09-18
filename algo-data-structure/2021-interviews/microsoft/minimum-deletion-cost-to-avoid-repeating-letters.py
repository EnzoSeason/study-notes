from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
    """

    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) <= 1:
            return 0

        i = 0
        total = 0

        while i < len(s):
            j = i + 1
            local_max = cost[i]
            while j < len(s) and s[j] == s[i]:
                local_max = max(local_max, cost[j])
                j += 1
            if j != i + 1:
                total += sum(cost[i:j]) - local_max
            i = j

        return total