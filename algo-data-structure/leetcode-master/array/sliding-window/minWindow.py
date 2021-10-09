class Solution:
    """
    https://leetcode.com/problems/minimum-window-substring/
    """

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        targets = {}
        for c in t:
            targets[c] = targets.get(c, 0) + 1
        required = len(targets)

        window = {}
        #  the number of satisfied char
        #  t: {a:1, b:2}, s: {a:1, b:1} => uniq_count == 1.
        #  Because only "a" is satisfied.
        uniq_count = 0
        min_len = float("inf")
        start, end = 0, 0

        l, r = 0, 0
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in targets and window[s[r]] == targets[s[r]]:
                uniq_count += 1
            #  When the window contains all the charactors in the t.
            #  reduce the window size.
            while l <= r and uniq_count == required:
                #  update the window size
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start, end = l, r
                #  reduce the window size
                window[s[l]] -= 1
                if s[l] in targets and window[s[l]] < targets[s[l]]:
                    uniq_count -= 1

                l += 1

            r += 1

        return s[start : end + 1] if min_len != float("inf") else ""
