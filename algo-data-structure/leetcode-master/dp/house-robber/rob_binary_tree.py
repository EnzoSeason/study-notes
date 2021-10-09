from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDP:
    """
    https://leetcode.com/problems/house-robber-iii/
    """

    def rob(self, root: TreeNode) -> int:
        return max(self.robTree(root))

    def robTree(self, root: TreeNode) -> List[int]:
        """
        return [max_not_rob_root, max_rob_root]
        """

        if not root:
            return [0, 0]

        left = self.robTree(root.left)
        right = self.robTree(root.right)

        return [max(left) + max(right), root.val + left[0] + right[0]]


class SolutionRE:
    def __init__(self) -> None:
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root in self.memo:
            return self.memo[root]

        if not root.left and not root.right:
            self.memo[root] = root.val
            return root.val

        # not rob current node
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)

        # rob current node
        val2 = self.rob(root.left) + self.rob(root.right)

        self.memo[root] = max(val1, val2)
        return max(val1, val2)