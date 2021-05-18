from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        results = [1 for _ in range(n)]

        for i in range(1, len(nums)):
            results[i] = (
                max([results[j] if nums[j] < nums[i] else 0 for j in range(i)]) + 1
            )
        print(results)
        return max(results)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print(s.lengthOfLIS(nums))