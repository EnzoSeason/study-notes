from typing import List


class Solution:
    """
    kmp: use PMT
    """

    def getPMT(self, s: str) -> List[int]:
        pmt = [0] * len(s)
        i, j = 1, 0

        while i < len(s):
            while j > 0 and s[i] != s[j]:
                j = pmt[j - 1]

            if s[i] == s[j]:
                j += 1

            pmt[i] = j
            i += 1

        return pmt

    def strStr(self, haystack: str, needle: str) -> int:
        pmt = self.getPMT(needle)
        i, j = 0, 0

        while i < len(haystack) and j < len(needle):
            while j > 0 and haystack[i] != needle[j]:
                j = pmt[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            i += 1

        return i - j if j == len(needle) else -1