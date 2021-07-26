class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0.0

    def dfs(self, root: TreeNode) -> tuple:
        if not root:
            return (0, 0.0)
        n_left, sum_left = self.dfs(root.left)
        n_right, sum_right = self.dfs(root.right)

        n = n_left + n_right + 1
        s = sum_left + sum_right + root.val
        self.res = max(self.res, s / n)

        return (n, s)

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.dfs(root)
        return self.res