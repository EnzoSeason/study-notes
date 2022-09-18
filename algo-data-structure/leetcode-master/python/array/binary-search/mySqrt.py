class Solution:
    """
    https://leetcode.com/problems/sqrtx/
    """

    def mySqrt(self, target: int) -> int:
        if target <= 1:
            return target

        l, r = 1, target
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid < target:
                if (mid + 1) * (mid + 1) > target:
                    return mid
                l = mid + 1
            elif mid * mid > target:
                r = mid - 1
            else:
                return mid