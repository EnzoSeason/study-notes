class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    """

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        if not root:
            return

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        ## 1. root is None
        ## 2. root is p or q
        ## 3. root is between the p and q
        return root