from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    
    if n <= 1:
        return nums
    
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    return nums