from typing import List
from random import randint


def bin_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    #   init bins
    N = 5
    bins = [[] for _ in range(N)]
    max_num = max(nums)
    res = []

    for num in nums:
        for i in range(N):
            if i == 0 and num < (i + 1) * max_num // N:
                bins[i].append(num)
            elif i == N - 1 and i * max_num // N <= num:
                bins[i].append(num)
            elif i * max_num // N <= num < (i + 1) * max_num // N:
                bins[i].append(num)
    
    print("Bins: {}".format(bins))
    for bin in bins:
        res += quick_sort(bin)

    return res


def quick_sort(nums: List[int]) -> List[int]:
    _quick_sort_worker(nums, 0, len(nums))
    return nums


def _quick_sort_worker(nums: List[int], start: int, end: int) -> None:
    if start >= end - 1:
        return
    pivot = _partition(nums, start, end)
    _quick_sort_worker(nums, start, pivot)
    _quick_sort_worker(nums, pivot + 1, end)


def _partition(nums: List[int], start: int, end: int) -> int:
    k = randint(start, end - 1)
    pivot = nums[k]
    nums[k], nums[end - 1] = nums[end - 1], nums[k]

    pivot_idx = start
    for i in range(start, end - 1):
        if nums[i] < pivot:
            nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
            pivot_idx += 1

    nums[pivot_idx], nums[end - 1] = nums[end - 1], nums[pivot_idx]

    return pivot_idx


if __name__ == "__main__":
    arr = [11, 8, 3, 9, 7, 1, 2, 5]

    print("Sort starts")
    sorted_arr = bin_sort(arr)
    print("Sort ends")

    print("orignal: ", arr)
    print("sorted: ", sorted_arr)
