from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    """

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        is_reversed = -1

        while queue:
            n = len(queue)
            layer = deque([])
            for _ in range(n):
                node = queue.popleft()
                if is_reversed < 0:
                    layer.append(node.val)
                else:
                    layer.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(layer)
            is_reversed *= -1

        return res