from typing import List


def binary_search_recursive(nums: List[int], num: int) -> bool:
    if len(nums) == 0:
        return False

    mid_idx = len(nums) // 2
    if num == nums[mid_idx]:
        return True
    if num < nums[mid_idx]:
        return binary_search_recursive(nums[0:mid_idx], num)
    if num > nums[mid_idx]:
        return binary_search_recursive(nums[mid_idx+1:len(nums)], num)


if __name__ == "__main__":
    nums = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    num = 67

    print(nums)
    is_finded = binary_search_recursive(nums, num)
    print("{} is finded ? {}".format(num, is_finded))
