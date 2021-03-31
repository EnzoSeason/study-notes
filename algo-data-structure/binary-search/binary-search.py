from typing import List


def binary_search(nums: List[int], num: int) -> bool:
    my_nums = nums.copy()

    while len(my_nums) != 0:
        mid_idx = len(my_nums) // 2
        
        if num == my_nums[mid_idx]:
            return True
        if num < my_nums[mid_idx]:
            my_nums = my_nums[0:mid_idx]
        if num > my_nums[mid_idx]:
            my_nums = my_nums[mid_idx+1:len(my_nums)]
    
    return False



if __name__ == "__main__":
    nums = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    num = 67
    
    print(nums)
    is_finded = binary_search(nums, num)
    print("{} is finded ? {}".format(num, is_finded))