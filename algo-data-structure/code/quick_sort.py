import random
from typing import List


def quick_sort(arr: List[int]):
    copied_arr = arr.copy()
    n = len(copied_arr)

    _quick_sort_worker(copied_arr, 0, n)
    return copied_arr

def _quick_sort_worker(arr: List[int], start: int, end: int) -> None:
    if start >= end - 1: 
        return
    
    pivot_idx = _partition(arr, start, end)
    print(arr, 'pivot is {} (index)'.format(pivot_idx))
    _quick_sort_worker(arr, start, pivot_idx)
    _quick_sort_worker(arr, pivot_idx+1, end)

def _partition(arr: List[int], start: int, end: int) -> int:
    '''
    Tricky method:

    1. choose a random item in the array, and put it at the first / last position
    2. traverse the rest of array
    '''
    k = random.randint(start, end - 1)
    arr[k], arr[end - 1] = arr[end - 1], arr[k]
    pivot_idx = start

    for i in range(start, end - 1):
        if arr[i] > arr[end - 1]:
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
            pivot_idx += 1
        
    arr[end - 1], arr[pivot_idx] = arr[pivot_idx], arr[end - 1]
    
    return pivot_idx


if __name__ == "__main__":
    arr = [11, 8, 3, 9, 7, 1, 2, 5]
    
    print('Sort starts')
    sorted_arr = quick_sort(arr)
    print('Sort ends')
    
    print('orignal: ', arr)
    print('sorted: ', sorted_arr)
