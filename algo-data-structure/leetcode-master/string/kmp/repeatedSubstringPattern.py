class Solution:
    """
    https://leetcode.com/problems/repeated-substring-pattern/
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        next_arr = [-1] * (len(s) + 1)
        j = -1

        for i in range(len(s)):
            while j >= 0 and s[i] != s[j]:
                j = next_arr[j]
            i += 1
            j += 1
            next_arr[i] = j

        #  s =            "a  b  c  a  b  c  a  b  c  a  b  c"
        #  next_arr = [-1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #  next_arr[n] != 0 => The last char is in the substring.
        #  n % (n - next_arr[n]) == 0 => The shortest substring is s[0: (n - next_arr[n])].
        n = len(s)
        return next_arr[n] != 0 and n % (n - next_arr[n]) == 0