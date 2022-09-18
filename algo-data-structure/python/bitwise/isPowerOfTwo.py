class Solution:
    """
    https://leetcode.com/problems/power-of-two/
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n & (n - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(8))