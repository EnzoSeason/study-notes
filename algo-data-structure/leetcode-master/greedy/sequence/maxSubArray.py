from typing import List


class SolutionGreedy:
    """
    https://leetcode.com/problems/maximum-subarray/

    When local max <= 0, reset it as 0.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = nums[0]

        for num in nums:
            local_max += num
            global_max = max(local_max, global_max)

            if local_max <= 0:
                #  reset local_max
                local_max = 0

        return global_max


class SolutionDP:
    """
    https://leetcode.com/problems/maximum-subarray/
    """

    def maxSubArray(self, nums: List[int]) -> int:
        local_max = [0] * len(nums)  #  the max in nums[:i]
        local_max[0] = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            local_max[i] = max(local_max[i - 1] + nums[i], nums[i])
            global_max = max(global_max, local_max[i])

        return global_max