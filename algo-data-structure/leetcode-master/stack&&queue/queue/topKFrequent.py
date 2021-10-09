import heapq
from typing import List


class MinHeap:
    def __init__(self, n: int) -> None:
        #  self.arr[0] is not used
        #  make sure (2 * i) and (2 * i + 1) are
        #  left, right child of (i)
        self.arr = [None] * (n + 1)
        self.n = n
        self.count = 0

    def push(self, val: tuple) -> None:
        if self.count == self.n:
            return

        self.count += 1
        self.arr[self.count] = val
        self.shiftup()

    def pop(self) -> tuple:
        if self.count == 0:
            return tuple()

        val = self.arr[1]
        #  replace the top by the last element
        self.arr[1] = self.arr[self.count]
        self.shiftdown(1)
        self.count -= 1

        return val

    def shiftup(self) -> None:
        i = self.count
        while i // 2 > 0:
            if self.arr[i // 2][0] > self.arr[i][0]:
                self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
                i //= 2
            else:
                break

    def shiftdown(self, i: int) -> None:
        l, r = 2 * i, 2 * i + 1
        min_idx = i
        
        if l <= self.count and self.arr[l][0] < self.arr[min_idx][0]:
            min_idx = l
        if r <= self.count and self.arr[r][0] < self.arr[min_idx][0]:
            min_idx = r
            
        if min_idx == i:
            return
        
        self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        self.shiftdown(min_idx)

    def getArray(self) -> list:
        return self.arr[1 : self.count + 1]
    
    def getTop(self) -> tuple:
        return self.arr[1]


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements/
    """

    def topKFrequent_minHeap(self, nums: List[int], k: int) -> List[int]:
        """
        use minHeap to sort the frequence
        """

        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1

        minHeap = MinHeap(k)
        for num, freq in cache.items():
            if (
                len(minHeap.getArray()) == k
                and minHeap.getTop()
                and minHeap.getTop()[0] < freq
            ):
                minHeap.pop()
            minHeap.push((freq, num))

        return [item[1] for item in minHeap.getArray()]

    def topKFrequent_heapq(self, nums: List[int], k: int) -> List[int]:
        """
        use heapq of python, which is a minHeap
        """

        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1

        minHeap = []
        for num, freq in cache.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [item[1] for item in minHeap]

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1

        sorted_key = list(sorted(cache, key=cache.get))
        return sorted_key[len(sorted_key) - 1 :]
