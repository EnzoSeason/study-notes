class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    https://leetcode.com/problems/symmetric-tree/

    use backtracing

    > Postorder traversal is a backtracing.
    """

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None or right is None:
            return left is None and right is None

        if left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)

        return outside and inside

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.compare(root.left, root.right)


class Solution2:
    """
    https://leetcode.com/problems/symmetric-tree/

    Iteration version of Solution1
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [root.left, root.right]

        while stack:
            right = stack.pop()
            left = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            stack.append(left.left)
            stack.append(right.right)

            stack.append(left.right)
            stack.append(right.left)

        return True