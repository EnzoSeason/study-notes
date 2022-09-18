from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/binary-tree-inorder-traversal/
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack = []
        res = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res