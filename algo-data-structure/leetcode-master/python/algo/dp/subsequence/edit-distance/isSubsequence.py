class SolutionDP:
    """
    https://leetcode.com/problems/is-subsequence/
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 > n2:
            return False

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1] == n1


class SolutionTwoPointers:
    """
    https://leetcode.com/problems/is-subsequence/
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 > n2:
            return False

        i, j = 0, 0
        while i < n1 and j < n2:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == n1