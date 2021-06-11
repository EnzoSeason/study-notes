class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeftLevel(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + self.getLeftLevel(node.left)
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.getLeftLevel(root.left)
        right = self.getLeftLevel(root.right)
        
        # return current node + nb of node in the left child tree + nb of node in the right child tree
        # The nb of node of a perfect binary tree = 2 ^ level - 1, level = depth + 1
        if left == right:
            # The left child tree must be a perfect binary tree.
            # The next tree to check is the right child tree.
            return 1 + ((1 << left) - 1) + self.countNodes(root.right)
        else:
            # The right child tree must be a perfect binary tree.
            # right = left - 1
            # The next tree to check is the left child tree.
            return 1 + self.countNodes(root.left) + ((1 << right) - 1)