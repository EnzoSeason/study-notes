from typing import List


class Solution:
    """
    https://leetcode.com/problems/non-overlapping-intervals/
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        upper_bound = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < upper_bound:
                count += 1
            else:
                upper_bound = intervals[i][1]

        return count