from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(n):
        has_swap = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[i], nums[j] = nums[j], nums[i]
                has_swap = True
        if not has_swap:
            break
    
    return nums