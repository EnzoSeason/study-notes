from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )

    def postorderTraversal_iter(self, root: TreeNode) -> List[int]:
        """
        1. create the order: mid->right->left. (preorder is mid->left->right)
        2. reverse the order
        """

        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            # Attention: the order here is different from that of the preorder.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]