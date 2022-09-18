from typing import List


def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
    return -1



if __name__ == "__main__":
    nums = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    num = 67
    
    print(nums)
    idx = binary_search(nums, num)
    print("{} is finded in ? {}".format(num, idx))