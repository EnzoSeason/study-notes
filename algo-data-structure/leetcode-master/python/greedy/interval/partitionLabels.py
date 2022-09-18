from typing import List


class Solution:
    """
    https://leetcode.com/problems/partition-labels/
    """

    def partitionLabels(self, s: str) -> List[int]:
        # cache the last apperance position of each char
        end_pos = [0] * 26
        for i in range(len(s)):
            end_pos[ord(s[i]) - ord("a")] = i

        res = []
        upper_bound = 0
        for i in range(len(s)):
            pos = end_pos[ord(s[i]) - ord("a")]
            # update upper_bound
            upper_bound = max(upper_bound, pos)
            if i == upper_bound:
                # meet the upper bound
                # split the string
                lower_bound = sum(res)
                res.append(upper_bound - lower_bound + 1)
        return res