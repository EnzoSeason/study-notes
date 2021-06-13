from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    https://leetcode.com/problems/validate-binary-search-tree/
    """

    def dfs(self, node: TreeNode, min_val: int, max_val: int) -> bool:
        if not node:
            return True

        if min_val < node.val < max_val:
            # The left subtree of a node contains only nodes with keys less than the node's key
            left = self.dfs(node.left, min_val, node.val)
            # The right subtree of a node contains only nodes with keys greater than the node's key.
            right = self.dfs(node.right, node.val, max_val)
            # Both the left and right subtrees must also be binary search trees.
            return left and right

        return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

class Solution2:
    """
    use inorder traversal.
    check leftMax < curr.val
    """

    def __init__(self) -> None:
        self.leftMax = float("-inf")
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # check left child tree
        left = self.isValidBST(root.left)
        if not left:
            return False
        
        # check current node
        if root.val <= self.leftMax:
            return False
        self.leftMax = root.val
        
        # check right child tree
        return self.isValidBST(root.right)


class Solution3:
    """
    Use inorder traversal
    The result array must be ASC.
    """

    def inorder(self, node: TreeNode) -> List[int]:
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        inorder_arr = self.inorder(root)
        for i in range(1, len(inorder_arr)):
            if inorder_arr[i - 1] >= inorder_arr[i]:
                return False
        return True