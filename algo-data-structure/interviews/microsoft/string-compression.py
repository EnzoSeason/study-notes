from typing import List


class Solution:
    """
    https://leetcode.com/problems/string-compression/

    fast-slow pointers
    """

    def partial_compress(self, chars: List[str], i: int, count: int) -> int:
        if count > 1:
            for num in str(count):
                chars[i + 1] = num
                i += 1
        return i + 1

    def compress(self, chars: List[str]) -> int:
        fast, slow = 0, 0
        count = 0

        while fast < len(chars):
            if chars[fast] == chars[slow]:
                fast += 1
                count += 1
            else:
                slow = self.partial_compress(chars, slow, count)
                chars[slow] = chars[fast]
                count = 0
                
        return self.partial_compress(chars, slow, count)