class SolutionDP:
    """
    https://leetcode.com/problems/edit-distance/
    """

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        # dp[i][j] means
        # the minimum number of operations required to convert
        # word1[0:i+1] to word1[0:j+1]
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
                    insert = dp[i][j - 1] + 1
                    delete = dp[i - 1][j] + 1
                    replace = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert, delete, replace)

        return dp[-1][-1]


class SolutionDP2:
    """
    https://leetcode.com/problems/edit-distance/

    Since dp[i] only depends on dp[i - 1],
    we use prev to cache dp[i - 1].
    """

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        prev = [i for i in range(n2 + 1)]
        curr = [0 for _ in range(n2 + 1)]

        for i in range(1, n1 + 1):
            curr[0] = i

            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insert = curr[j - 1] + 1
                    delete = prev[j] + 1
                    replace = prev[j - 1] + 1
                    curr[j] = min(insert, delete, replace)

            prev, curr = curr, [0 for _ in range(n2 + 1)]

        return prev[-1]


class SolutionDP3:
    """
    https://leetcode.com/problems/edit-distance/

    Since dp[i] only depends on dp[i - 1],
    we use a temporary variable to cache dp[i - 1][j - 1].
    """

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        curr = [i for i in range(n2 + 1)]

        for i in range(1, n1 + 1):
            prev = curr[0]
            curr[0] = i

            for j in range(1, n2 + 1):
                cache = curr[j]
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev
                else:
                    insert = curr[j - 1] + 1
                    delete = curr[j] + 1
                    replace = prev + 1
                    curr[j] = min(insert, delete, replace)

                prev = cache

        return curr[-1]