class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/delete-node-in-a-bst/
    """

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # put left child tree under 
            # the leftest part of right child tree.
            q = root.right
            while q.left:
                q = q.left
            q.left, root = root.left, root.right

        return root