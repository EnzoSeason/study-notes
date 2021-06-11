class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, node: TreeNode) -> int:
        if not node:
            return 0

        left, right = self.getDepth(node.left), self.getDepth(node.right)

        if left == -1 or right == -1:
            return -1

        return 1 + max(left, right) if abs(left - right) <= 1 else -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.getDepth(root) != -1