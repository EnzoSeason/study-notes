class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n != m:
            return False

        cache = [0] * 26

        for i in range(n):
            cache[ord(s[i]) - ord("a")] += 1
            cache[ord(t[i]) - ord("a")] -= 1

        return not any(cache)