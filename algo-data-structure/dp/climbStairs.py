class SolutionDP1:
    """
    https://leetcode.com/problems/climbing-stairs/
    using DP with an array
    """
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

class SolutionBackTracking:
    """
    https://leetcode.com/problems/climbing-stairs/
    using Back Tracking with a memo array
    """
    def __init__(self) -> None:
        self.memo = []
    
    def _re(self, i: int) -> None:
        if self.memo[i]:
            return self.memo[i]
        self.memo[i] = self._re(i-1) + self._re(i-2)
        return self.memo[i]
        
        
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        self.memo = [0 for _ in range(n+1)]
        self.memo[1] = 1
        self.memo[2] = 2
        
        return self._re(n)

class SolutionDP2:
    """
    https://leetcode.com/problems/climbing-stairs/
    using DP with 2 variable
    """
    def climbStairs(self, n: int) -> int:        
        prev = 1
        curr = 1
        
        for _ in range(1, n):
            prev, curr = curr, prev + curr
        
        return curr