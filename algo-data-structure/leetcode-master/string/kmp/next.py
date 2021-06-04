from typing import List


class Solution:
    """
    KMP: next == [-1] + PMT 
    """
    def getNext(self, s: str) -> List[int]:
        next_arr = [-1] * (len(s) + 1)
        i, j = 0, -1

        while i < len(s):
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                next_arr[i] = j
            else:
                j = next_arr[j]
        
        return next_arr
    
    def strStr(self, haystack: str, needle: str) -> int:
        next_arr = self.getNext(needle)
        i, j = 0, 0
        
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        
        return i - j if j == len(needle) else -1
