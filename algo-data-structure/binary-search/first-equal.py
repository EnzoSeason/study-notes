from typing import List


def first_equal(nums: List[int], given: int) -> int:
    low = 0
    high = len(nums)

    while low <= high:
        mid = low + (high - low) // 2
        if given > nums[mid]:
            low = mid + 1
        elif given < nums[mid]:
            high = mid - 1
        else:
            if mid == 0 or nums[mid-1] != given:
                return mid
            else:
                high = mid - 1

    return -1  


if __name__ == "__main__":
    nums = [8, 11, 19, 23, 27, 33, 45, 55, 67, 67, 67, 98]
    num = 67

    print(nums)
    pos = first_equal(nums, num)
    print("{}: first find in {}".format(num, pos))