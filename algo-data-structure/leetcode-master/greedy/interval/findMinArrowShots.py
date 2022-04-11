from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

    update the upper bound.
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorted by upper bound in ASC
        points = sorted(points, key=lambda x: x[1])
        count = 1
        upper_bound = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > upper_bound:
                count += 1
                upper_bound = points[i][1]

        return count