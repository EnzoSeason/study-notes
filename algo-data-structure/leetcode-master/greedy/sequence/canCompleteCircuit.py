from typing import List


class SolutionBrute:
    """
    https://leetcode.com/problems/gas-station/
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start, n = 0, len(gas)
        
        while start < n:
            i = start
            while tank + gas[i] >= cost[i]:
                tank = tank + gas[i] - cost[i]
                i = (i + 1) % n
                
                if i == start:
                    return start
            tank = 0
            start += 1
        
        return -1


class SolutionGreedy:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, n = 0, len(gas)
        global_rest, local_rest = 0, 0
        
        for i in range(n):
            global_rest += gas[i] - cost[i]
            local_rest += gas[i] - cost[i]
            # Once local_rest < 0, the circuit can't be completed.
            # So, we need to update start and local_rest.
            if local_rest < 0:
                local_rest = 0
                start = i + 1
        
        return start % n if global_rest >= 0 else -1