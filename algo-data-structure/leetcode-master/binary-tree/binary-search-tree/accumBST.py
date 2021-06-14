class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/convert-bst-to-greater-tree/
    """

    def __init__(self) -> None:
        self.prev_val = 0

    def traverse(self, root: TreeNode) -> None:
        """
        right -> mid -> left
        """

        if not root:
            return

        self.traverse(root.right)

        root.val += self.prev_val
        self.prev_val = root.val

        self.traverse(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root