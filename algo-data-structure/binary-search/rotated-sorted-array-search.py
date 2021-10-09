from typing import List

def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target: return mid

        is_mid_bigger = nums[mid] >= nums[0]
        is_target_bigger = target >= nums[0]

        if is_mid_bigger == is_target_bigger:
            #  mid and target are in the sorted ASC interval
            #  normal binary search
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if is_mid_bigger:
                low = mid + 1
            else:
                high = mid - 1

    return -1 

        

if __name__ == "__main__":
    nums = [7,0,1,2,3,4]
    target = 1

    idx = search(nums, target)
    print(idx)
    