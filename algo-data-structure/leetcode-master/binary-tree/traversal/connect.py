class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    """

    def connect_bfs(self, root: Node) -> Node:
        """
        Since it's perfect binary tree.
        BFS on all nodes except leaves
        """

        if not root:
            return root

        level_head = root
        while level_head.left:
            #  perfect binary tree
            #  If it has left child, it must have right child.
            parent = level_head
            while parent:
                parent.left.next = parent.right
                if parent.next:
                    #  perfect binary tree
                    #  All the nodes have 2 children, except the leaves.
                    parent.right.next = parent.next.left
                parent = parent.next
            level_head = level_head.left

        return root
    
    def connect_dfs(self, root: Node) -> Node:
        self.dfs(root, None)
        return root

    def dfs(self, curr_node: Node, next_node: Node) -> None:
        if not curr_node:
            return
        
        curr_node.next = next_node

        self.dfs(curr_node.left, curr_node.right)
        self.dfs(curr_node.right, next_node.left if next_node else None)