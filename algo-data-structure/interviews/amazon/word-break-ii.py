from typing import Dict, List


class SolutionDFS:
    def __init__(self) -> None:
        self.wordDict = []
        self.res = []

    def dfs(self, s: str, prev: List[str]) -> None:
        if not s:
            self.res.append(" ".join(prev))
            return

        for word in self.wordDict:
            if s[: len(word)] == word:  ## s.startswith(word)
                self.dfs(s[len(word) :], prev + [word])

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        self.res = []

        self.dfs(s, [])
        return self.res


class Solution:
    """
    DFS with cache
    """

    def __init__(self) -> None:
        self.wordDict = []

    def dfs(self, s: str, cache: Dict[str, List[str]]) -> List[str]:
        if not s:
            return []

        if s in cache:
            return cache[s]

        res = []
        for word in self.wordDict:
            if s.startswith(word):
                continue

            if len(s) == len(word):
                res.append(word)
            else:
                sub_res = self.dfs(s[len(word) :], cache)
                res += [word + " " + item for item in sub_res]

        cache[s] = res
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict

        return self.dfs(s, dict())