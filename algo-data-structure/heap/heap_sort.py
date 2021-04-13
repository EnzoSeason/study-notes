from typing import List
import numpy as np
import sys

sys.path.append('..')
from heap.MinHeap import MinHeap


def sort(nums: List[int]) -> List[int]:
    min_heap = MinHeap(len(nums))
    min_heap.build(nums)

    for i in range(len(nums), 0, -1):
        min_heap.arr[1], min_heap.arr[i] = min_heap.arr[i], min_heap.arr[1]
        min_heap.count -= 1
        min_heap.shiftdown(1)
    
    return min_heap.arr[1:]


if __name__ == "__main__":
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2,
           3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    print(np.sort(arr, kind='heapsort'))

    sorted_arr = sort(arr)

    print('orignal: ', arr)
    print('sorted: ', sorted_arr)
