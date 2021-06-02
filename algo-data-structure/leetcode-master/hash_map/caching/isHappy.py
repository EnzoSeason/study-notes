class Solution:
    """
    https://leetcode.com/problems/happy-number/
    """

    def happySum(self, n: int) -> int:
        mySum = 0
        while n:
            mySum += (n % 10) * (n % 10)
            n = n // 10
        return mySum

    def isHappy1(self, n: int) -> bool:
        """
        use a set to cache the internal results,
        which helps to detect the circle
        """
        res = set()

        while n != 1:
            if n in res:
                return False
            res.add(n)
            n = self.happySum(n)

        return True

    def isHappy2(self, n: int) -> bool:
        """
        use Floyd's tortoise and hare (https://en.wikipedia.org/wiki/Cycle_detection)

        fast_move = 2 * slow_move
        When fast == slow, it detects a circle.
        """

        slow, fast = n, self.happySum(n)

        while slow != fast:
            if fast == 1:
                return True
            slow = self.happySum(slow)
            for _ in range(2):
                fast = self.happySum(fast)

        return True if fast == 1 else False