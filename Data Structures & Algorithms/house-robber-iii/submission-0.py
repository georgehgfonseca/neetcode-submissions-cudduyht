from functools import cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # either rob or not current node

        @cache
        def dfs(root, robbedLast):
            if not root:
                return 0

            if robbedLast:
                return dfs(root.left, False) + dfs(root.right, False)
            return max(root.val + dfs(root.left, True) + dfs(root.right, True), dfs(root.left, False) + dfs(root.right, False))

        return dfs(root, False)
        