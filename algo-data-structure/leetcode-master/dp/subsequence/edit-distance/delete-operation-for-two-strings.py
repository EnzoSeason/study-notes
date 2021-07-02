class Solution:
    """
    https://leetcode.com/problems/delete-operation-for-two-strings/
    """

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete_char_i = dp[i - 1][j] + 1
                    delete_char_j = dp[i][j - 1] + 1
                    delete_char_i_j = dp[i - 1][j - 1] + 2
                    dp[i][j] = min(delete_char_i, delete_char_j, delete_char_i_j)
        return dp[-1][-1]