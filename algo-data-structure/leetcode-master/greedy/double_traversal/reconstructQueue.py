from typing import List


class Solution:
    """
    https://leetcode.com/problems/queue-reconstruction-by-height/
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ## sort by
        ## First item in DESC, then
        ## Second item in ASC
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        res = []
        for p in people:
            res.insert(p[1], p)
        return res