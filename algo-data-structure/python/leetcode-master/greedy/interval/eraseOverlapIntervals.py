from typing import List


class Solution:
    """
    https://leetcode.com/problems/non-overlapping-intervals/
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorted by upper bound in ASC
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 0 # nb of removed intervals
        upper_bound = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < upper_bound:
                # remove the interval
                count += 1
            else:
                # keep the interval
                # update upper_bound
                upper_bound = intervals[i][1]

        return count