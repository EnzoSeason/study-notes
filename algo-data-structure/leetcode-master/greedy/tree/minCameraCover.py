class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.covered = set([None])  #  None is covered
        self.nb = 0

    def dfs(self, node: TreeNode, parent: TreeNode) -> None:
        if not node:
            return

        if node.left:
            self.dfs(node.left, node)
        if node.right:
            self.dfs(node.right, node)

        #  case 1: If root is not covered, add an camera at root
        #  case 2: If one of the children isn't covered, add an camera at the current node.
        if (
            not parent
            and node not in self.covered
            or node.left not in self.covered
            or node.right not in self.covered
        ):
            self.nb += 1
            #  add more nodes into covered set.
            self.covered |= set([parent, node, node.left, node.right])

    def minCameraCover(self, root: TreeNode) -> int:
        self.dfs(root, None)
        return self.nb