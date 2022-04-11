from typing import List


class SolutionDP:
    """
    use 2 DP table to keep the left and right boundaries.
    """

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0

        max_left, max_right = [0] * n, [0] * n
        max_left[0], max_right[-1] = height[0], height[-1]

        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]

        return res


class SolutionTwoPointers:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0

        res = 0
        l, r = 0, n - 1
        left_boundary, right_boundary = 0, 0

        while l < r:
            if height[l] < height[r]:  ##  It makes sure we have the min boundary.
                if height[l] >= left_boundary:
                    left_boundary = height[l]
                else:
                    res += left_boundary - height[l]
                l += 1
            else:
                if height[r] >= right_boundary:
                    right_boundary = height[r]
                else:
                    res += right_boundary - height[r]
                r -= 1

        return res


class SolutionStack:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        
        res = 0
        stack = []
        i = 0
        
        while i < n:
            while stack and height[i] > height[stack[-1]]: ## right boundary found
                top = stack.pop() ## the bottom is height[top]
                if not stack:
                    break
                distance = i - stack[-1] - 1 ## the distance between the left boundary and right boundary
                res += distance * (min(height[i], height[stack[-1]]) - height[top])
            stack.append(i)
            i += 1
        
        return res