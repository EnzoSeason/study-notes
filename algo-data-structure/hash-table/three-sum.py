from typing import List


def threeSum_way1(self, nums: List[int]) -> List[List[int]]:
    """
    First loop: v in nums
    Second loop: find x and -v-x with a hash map
    O(n^2)
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    
    return list(res)

def threeSum_way2(self, nums: List[int]) -> List[List[int]]:
    """
    First loop: index is i
    Second loop: from edges, left and right, to the centre, find nums[i] + nums[l] + nums[r] == 0
    O(n^2)
    """
    if len(nums) < 3:
        return []
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            s =  nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            if s < 0:
                l += 1
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res