from typing import List

## https://leetcode.com/problems/move-zeroes/


class Solution1:
    """
    use fast-slow pointers
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


class Solution2:
    """
    using the idea of Bubble Sort
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time Complexity: O(n^2)
        """
        i, swap_count = 0, 0
        while i < len(nums) - swap_count:
            print(nums)
            if nums[i] == 0:
                for j in range(i, len(nums) - 1 - swap_count):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap_count += 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    s1 = Solution1()
    s1.moveZeroes(nums)