from typing import List, Optional

class MaxHeap:
    def __init__(self, n: int) -> None:
        """
        ## Arributes
        - n: the capacity of the MinHeap
        - arr: the array that contains heap's data
        - count: current volume of the heap
        """
        self.n = n
        self.arr = [None for _ in range(n+1)]
        self.count = 0

    def __str__(self) -> str:
        s = "MaxHeap: \n"
        s += "n = {}\n".format(self.n)
        s += "heap = {}\n".format(self.arr[1:self.count+1])
        return s

    def shiftdown(self, top: int):
        '''
        from top to bottom heapify for a min-heap
        '''
        i = smaller_child_index = top
        while True:
            left, right = 2*i, 2*i+1
            if left <= self.count and self.arr[smaller_child_index] < self.arr[left]:
                smaller_child_index = left
            if right <= self.count and self.arr[smaller_child_index] < self.arr[right]:
                smaller_child_index = right
            if smaller_child_index == i:
                break
            self.arr[i], self.arr[smaller_child_index] = self.arr[smaller_child_index], self.arr[i]
            i = smaller_child_index

    def shiftup(self):
        '''
        from bottom to top heapify for a min-heap
        '''
        i = self.count
        while i // 2 != 0:
            if self.arr[i//2] < self.arr[i]:
                self.arr[i], self.arr[i//2] = self.arr[i//2], self.arr[i]
                i = i // 2
            else:
                break
    
    def build(self, arr: List[int]):
        if len(arr) > self.n:
            return
        self.arr = [None] + arr
        self.count = len(arr)
        for i in range(self.count // 2, 0, -1):
            self.shiftdown(i)


    def push(self, num: int) -> None:
        if self.count == self.n:
            return
        self.count += 1
        self.arr[self.count] = num
        self.shiftup()

    def pop(self) -> Optional[int]:
        if self.count == 0:
            return None
        val = self.arr[1]
        self.arr[1] = self.arr[self.count]
        self.count -= 1
        self.shiftdown(1)
        return val