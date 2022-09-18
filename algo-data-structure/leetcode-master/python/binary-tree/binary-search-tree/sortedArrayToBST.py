from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

    using binary search, the interval is [left, right].
    """

    def build(self, nums: List[int], left: int, right: int) -> None:
        if left > right:
            return

        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])

        root.left = self.build(nums, left, mid - 1)
        root.right = self.build(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)