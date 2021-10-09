#  https://leetcode.com/problems/maximum-depth-of-binary-tree/
#  https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """
    use DFS
    """
    if root is None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)

def minDepth(root: TreeNode) -> int:
    """
    use DFS
    """
    if root is None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    if root.left is None:
        return 1 + right
    if root.right is None:
        return 1 + left
    return 1 + min(left, right)


def minDepth_bfs(root: TreeNode) -> int:
    """
    use BFS
    """
    if root is None:
        return 0

    queue = []
    queue.append(root)
    depth = 0

    while queue:
        n = len(queue)
        depth += 1
        for _ in range(n):
            node = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
