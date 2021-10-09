from typing import List


class Solution:
    """
    https://leetcode.com/problems/word-break/submissions/
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1): #  traverse the capacity of the pack
            for word in wordDict: #  travarse the word.
                if s[i : i + len(word)] == word and dp[i]: 
                    #  Current and previous words are found.
                    #  Set current status to True
                    dp[i + len(word)] = True

        return dp[len(s)]