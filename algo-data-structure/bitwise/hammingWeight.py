class Solution:
    """
    https://leetcode.com/problems/number-of-1-bits/
    """
    def hammingWeight_method1(self, n: int) -> int:
        """
        use mask to check each bit
        """
        count = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count

    def hammingWeight_method2(self, n: int) -> int:
        """
        use n & (n-1) to remove the lowest 1
        """
        count = 0
        while n != 0:
            count += 1
            n = n & (n-1)
        return count
