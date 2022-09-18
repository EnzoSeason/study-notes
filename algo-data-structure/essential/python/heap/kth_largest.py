import numpy as np
import sys

sys.path.append('..')
from heap.MinHeap import MinHeap

def kth_largest(nums, k):
    min_heap = MinHeap(k)
    min_heap.build(nums[0:k])

    for i in range(k, len(nums)):
        if nums[i] > min_heap.arr[1]:
            min_heap.pop()
            min_heap.push(nums[i])

    print(min_heap)
    return min_heap.arr[1]


if __name__ == "__main__":
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2,
           3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    print(np.sort(arr))
    print(np.sort(arr)[-20])
    k = 20

    item = kth_largest(arr, k)

    print('orignal: ', arr)
    print('k: ', k)
    print('item: ', item)
