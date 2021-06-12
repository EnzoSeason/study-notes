from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/find-bottom-left-tree-value/
    """

    def __init__(self) -> None:
        self.maxDepth = -1
        self.res = 0

    def dfs(self, node: TreeNode, depth: int) -> None:
        if not node.left and not node.right:
            # update the res once the depth is increased.
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.res = node.val
        # The order is important.
        #  The left is first to update.
        if node.left:
            self.dfs(node.left, depth + 1)
        if node.right:
            self.dfs(node.right, depth + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.res


class Solution2:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        res = root.val

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == 0:
                    res = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res