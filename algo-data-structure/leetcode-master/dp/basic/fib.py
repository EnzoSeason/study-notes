class SolutionDP:
    """
    https://leetcode.com/problems/fibonacci-number/
    """

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        f = [0] * (n + 1)
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        
        return f[n]

class Solution:
    """
    https://leetcode.com/problems/fibonacci-number/

    use 3 variables instead of an array
    """

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        res = 0
        for _ in range(2, n + 1):
            res = a + b
            a, b = b, res
        
        return res