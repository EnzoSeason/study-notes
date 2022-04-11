from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    copied_arr = arr.copy()
    n = len(copied_arr)

    _merge_sort_worker(copied_arr, 0, n)
    return copied_arr

def _merge_sort_worker(arr: List[int], start: int, end: int) -> None:
    '''
    merge sort the arr[start:end] recursively
    '''
    print(arr[start: end], start, end)
    if start >= end - 1: ## end-1 is the index of the last item is the array
        print('-----')
        return
    mid = start + (end - start) // 2
    _merge_sort_worker(arr, start, mid)
    _merge_sort_worker(arr, mid, end)
    _merge(arr, start, mid, end)

def _merge(arr: List[int], start: int, mid: int, end: int):
    '''
    merge arr[start:mid] and arr[mid:end]
    
    merged arr is sorted.
    '''
    i = start
    j = mid
    merged_arr = []

    while i != mid and j != end:
        if arr[i] > arr[j]:
            merged_arr.append(arr[j])
            j += 1
        else:
            merged_arr.append(arr[i])
            i += 1
    
    if i != mid: merged_arr.extend(arr[i:mid])
    if j != end: merged_arr.extend(arr[j:end])

    arr[start:end] = merged_arr
    


if __name__ == "__main__":
    arr = [11, 8, 3, 9, 7, 1, 2, 5]
    
    print('Sort starts')
    sorted_arr = merge_sort(arr)
    print('Sort ends')
    
    print('orignal: ', arr)
    print('sorted: ', sorted_arr)
