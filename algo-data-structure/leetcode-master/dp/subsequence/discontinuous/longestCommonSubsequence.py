class Solution:
    """
    https://leetcode.com/problems/longest-common-subsequence/
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        ## dp[0][:] and dp[:][0] are pivots.
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

class Solution:
    """
    https://leetcode.com/problems/longest-common-subsequence/

    Since we only need the status of i, i - 1, j, j - 1,
    we can reduce the dp dimensions into n * 2.
    """
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        if n1 < n2:
            return self.longestCommonSubsequence(text2, text1)
        
        dp = [[0 for _ in range(n2 + 1)] for _ in range(2)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                else:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
                    
        return dp[n1 % 2][-1]