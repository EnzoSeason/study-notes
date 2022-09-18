from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while fast < len(nums) and slow < len(nums) - 1:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


if __name__ == "__main__":
    nums = [1, 1, 2]

    s = Solution()
    print(s.removeDuplicates(nums))