from typing import List


def first_greater_equal(nums: List[int], given: int) -> int:
    low = 0
    high = len(nums)

    while low <= high:
        mid = low + (high - low) // 2
        if given <= nums[mid]:
            if mid == 0 or nums[mid-1] < given:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    
    return -1

if __name__ == "__main__":
    nums = [3 ,4, 6, 7, 10]
    num = 5

    print(nums)
    pos = first_greater_equal(nums, num)
    print("{}: first greater or equal find in {}".format(num, pos))