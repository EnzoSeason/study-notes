# leetcode 102: https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder_BFS(root: TreeNode) -> List[List[int]]:
    if root is None: return []

    res = []

    queue = []
    queue.append(root)

    while queue:
        level = []
        n = len(queue)

        for _ in range(n):
            node = queue.pop(0)
            level.append(node.val)

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        res.append(level)
    
    return res


def levelOrder_DFS(root: TreeNode) -> List[List[int]]:
    res = []
    _dfs(root, 1, res)
    return res

def _dfs(node: TreeNode, level: int, res: List[List[int]]) -> None:
    if node is None: return

    if len(res) < level:
        res.append([])
    
    res[level-1].append(node.val)

    _dfs(node.left, level+1, res)
    _dfs(node.right, level+1, res)