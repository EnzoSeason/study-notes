from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n <= 1:
        return nums

    for i in range(1, n):
        val = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > nums[i]:
                nums[j + 1] = nums[j]
            else:
                break
            j -= 1
        nums[j + 1] = val

    return nums