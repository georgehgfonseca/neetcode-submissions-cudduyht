# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(root, depth):
            if not root:
                self.ans = max(self.ans, depth)
                return

            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return self.ans
        