class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/delete-node-in-a-bst/
    """

    def deleteNode1(self, root: TreeNode, key: int) -> TreeNode:
        """
        put left child tree under the leftest part of right child tree.
        """

        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left

            # put left child tree under 
            # the leftest part of right child tree.
            q = root.right
            while q.left:
                q = q.left
            q.left, root = root.left, root.right

        return root
    
    def deleteNode2(self, root: TreeNode, key: int) -> TreeNode:
        """
        swap the searched node with the leftest leaf in the right child tree,
        then delete it.
        """

        if not root:
            return
        
        if root.val == key:
            # If the search node is a leaf
            # delete it
            if not root.right:
                return root.left
            
            # else, swap its value with 
            # the leftest leaf's value in the right child tree
            q = root.right
            while q.left:
                q = q.left
            root.val, q.val = q.val, root.val
        # Since the search tree is destroyed by the swap
        # We need to traverse the entire tree.
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        
        return root