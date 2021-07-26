from typing import List
import heapq

class Solution:
    """
    use hash map to cache the numbers of ints
    use min heap to count the removed unique ints
    """
    
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cache = dict()
        for num in arr:
            cache[num] = cache.get(num, 0) + 1
        cache = [(v, k) for k, v in sorted(cache.items(), key=lambda x: x[1])]
        heapq.heapify(cache)
        
        rest = k
        while rest > 0:
            rest -= heapq.heappop(cache)[0]
            
        return len(cache) + 1 if rest < 0 else len(cache)