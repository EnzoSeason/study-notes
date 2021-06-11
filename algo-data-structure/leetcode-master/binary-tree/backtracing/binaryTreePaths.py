class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/binary-tree-paths/
    """

    def dfs(self, node: TreeNode, path: List[str], res: List[str]) -> None:
        if not node.left and not node.right:
            res.append("->".join(path + [str(node.val)]))

        if node.left:
            self.dfs(node.left, path + [str(node.val)], res)
        if node.right:
            self.dfs(node.right, path + [str(node.val)], res)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []
        path = []
        self.dfs(root, path, res)

        return res