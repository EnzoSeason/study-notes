from typing import List


class Solution:
    """
    https://leetcode.com/problems/merge-intervals/
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals:
            if res[-1][1] >= interval[0]:
                # overlapped, update the upper bound
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                # not overlapped, add into result
                res.append(interval)
        
        return res