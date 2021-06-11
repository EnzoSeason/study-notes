from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    https://leetcode.com/problems/minimum-depth-of-binary-tree/

    DFS
    """

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:
            return 1 + left + right
        return 1 + min(left, right)


class Solution2:
    """
    https://leetcode.com/problems/minimum-depth-of-binary-tree/

    BFS
    """

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            n = len(queue)
            depth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth