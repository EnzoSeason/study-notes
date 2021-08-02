from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            cost += first + second
            heapq.heappush(sticks, first + second)

        return cost