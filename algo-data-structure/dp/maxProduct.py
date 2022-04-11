from typing import List


class SolutionRecursion:
    """
    https://leetcode.com/problems/maximum-product-subarray/

    use recursion:
    It's similar to Knapsack problem.
    There are 2 cases, multiply the current number or not.
    """

    def __init__(self) -> None:
        self.max_product = float("-inf")
        ## memo caches the states
        self.memo = []

    def _product(self, nums: List[int], curr_product: int, curr_idx: int) -> None:
        if curr_idx == len(nums):
            if curr_product > self.max_product:
                self.max_product = curr_product
            return

        ## check memo
        if curr_product in self.memo[curr_idx]:
            return
        self.memo[curr_idx].append(curr_product)

        ## multiply
        self._product(nums, curr_product * nums[curr_idx], curr_idx + 1)
        ## not multiply
        if curr_product > self.max_product:
            self.max_product = curr_product
        self._product(nums, nums[curr_idx], curr_idx + 1)

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        self.memo = [[] for _ in range(len(nums))]
        self._product(nums, nums[0], 1)
        return self.max_product


class SolutionDP:
    """
    https://leetcode.com/problems/maximum-product-subarray/

    use DP:
    DP keeps 2 states:
    - Max Product of current stage
    - Min Product of current stage, which is the max minus production

    Because Min Production multiply a negative number could create a Max Product
    """

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        ## we only keep the states of
        ## current stage and previous stage
        dp = [{"max": float("-inf"), "min": float("inf")} for _ in range(2)]
        dp[0]["max"], dp[0]["min"], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            ## curr and prev are overrided by each other.
            curr, prev = i % 2, (i - 1) % 2
            dp[curr]["max"] = max(dp[prev]["max"] * nums[i], dp[prev]["min"] * nums[i], nums[i])
            dp[curr]["min"] = min(dp[prev]["max"] * nums[i], dp[prev]["min"] * nums[i], nums[i])
            res = max(res, dp[curr]["max"])
        
        return res

