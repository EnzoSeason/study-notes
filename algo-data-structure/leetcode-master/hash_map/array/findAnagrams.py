from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

    idx: the idx of alphabet
    value: the count of alphabet
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        target_arr = [0] * 26
        search_arr = [0] * 26
        res = []

        for i in range(m):
            s_idx = ord(s[i]) - ord("a")
            search_arr[s_idx] += 1
            t_idx = ord(p[i]) - ord("a")
            target_arr[t_idx] += 1 

        for i in range(n - m + 1):
            if search_arr == target_arr:
                res.append(i)
            ## move the start of the sliding window
            window_start = ord(s[i]) - ord("a")
            search_arr[window_start] -= 1
            
            if i + m == n:
                break

            ## move the end of the sliding window
            window_end = ord(s[i + m]) - ord("a")
            search_arr[window_end] += 1

        return res