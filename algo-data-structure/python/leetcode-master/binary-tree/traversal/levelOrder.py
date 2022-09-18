from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal/
    """

    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res

    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level_worker(root, 1, res)
        return res

    def level_worker(self, node: TreeNode, level: int, res: List[List[int]]) -> None:
        if node is None:
            return
        if len(res) < level:
            res.append([])

        res[level - 1].append(node.val)

        self.level_worker(node.left, level + 1, res)
        self.level_worker(node.right, level + 1, res)
