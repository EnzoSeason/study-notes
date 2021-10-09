from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        
        #  create the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        #  split the Lists
        idx = inorder.index(root_val)
        root.left = self.buildTree(inorder[0:idx], postorder[0:idx])
        root.right = self.buildTree(inorder[idx + 1 :], postorder[idx:])

        return root