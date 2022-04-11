from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        rooms = []  # keep the end of intervals
        heapq.heappush(rooms, intervals[0][1])

        for interv in intervals[1:]:
            # compare the current start time with the min end time
            if rooms[0] <= interv[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interv[1])

        return len(rooms)