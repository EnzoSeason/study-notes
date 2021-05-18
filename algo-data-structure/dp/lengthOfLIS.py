from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/

    using DP
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


class Solution:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/

    maintain the LIS array using binary search
    """

    def __init__(self) -> None:
        self.LIS = []

    def updateLIS(self, target: int) -> None:
        n = len(self.LIS)
        if n == 0:
            self.LIS.append(target)
            return

        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target < self.LIS[mid]:
                high = mid - 1
            elif target > self.LIS[mid]:
                low = mid + 1
            else:
                return

        if low == n:
            self.LIS.append(target)
        else:
            self.LIS[low] = target

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        for num in nums:
            self.updateLIS(num)

        print(self.LIS)
        return len(self.LIS)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    s_dp = SolutionDP()
    print(s_dp.lengthOfLIS(nums))

    s = Solution()
    print(s.lengthOfLIS(nums))