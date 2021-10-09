class Solution:
    """
    https://leetcode.com/problems/flip-string-to-monotone-increasing/
    """
    
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        left_start, right_start = [0] * n, [0] * n
        res = n

        #  from left to right
        #  flip 0 to 1
        for i in range(1, n):
            left_start[i] = left_start[i - 1] + (0 if s[i - 1] == "0" else 1)

        #  from right to left
        #  flip 1 to 0
        for j in range(n - 2, -1, -1):
            right_start[j] = right_start[j + 1] + (0 if s[j + 1] == "1" else 1)

        for i in range(n):
            res = min(res, left_start[i] + right_start[i])

        return res