from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

    key: the alphabet
    value: the count of the alphabet
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        target_dict = {}
        search_dict = {}
        res = []

        for i in range(m):
            search_dict[s[i]] = search_dict.get(s[i], 0) + 1
            target_dict[p[i]] = target_dict.get(p[i], 0) + 1

        for i in range(n - m + 1):
            if search_dict == target_dict:
                res.append(i)

            search_dict[s[i]] -= 1
            if not search_dict[s[i]]:
                search_dict.pop(s[i])
            if i + m < n:
                search_dict[s[i + m]] = search_dict.get(s[i + m], 0) + 1

        return res