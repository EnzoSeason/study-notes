from typing import List
import sys
import numpy as np

sys.path.append('..')

from heap.MaxHeap import MaxHeap
from heap.MinHeap import MinHeap


def find_median(nums: List[int]):
    n = len(nums)
    k = n // 2
    min_heap = MinHeap(k)
    max_heap = MaxHeap(n-k)

    max_heap.push(nums[0])

    for i in range(1, n):
        if nums[i] < max_heap.arr[1]:
            if max_heap.count + 1 > n-k:
                item = max_heap.pop()
                min_heap.push(item)
            max_heap.push(nums[i])
        else:
            if min_heap.count + 1 > k:
                item = min_heap.pop()
                print('pop', item)
                max_heap.push(item)
            min_heap.push(nums[i])
        
        if max_heap.count > min_heap.count + 1:
            item = max_heap.pop()
            min_heap.push(item)
        
        if min_heap.count > max_heap.count:
            item = min_heap.pop()
            max_heap.push(item)



        print(max_heap)
        print(min_heap)
    
    return max_heap.arr[1]


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 7, 1, 2, 3, 8, 9, 9, 9]

    item = find_median(arr)

    print('sorted orignal: ', np.sort(arr))
    print('item: ', item)
