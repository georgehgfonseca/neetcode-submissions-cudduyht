# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        def helper(root):
            if not root:
                return True
            
            heightDiff = abs(height(root.left) - height(root.right))
            return heightDiff <= 1 and helper(root.left) and helper(root.right)
        
        return helper(root)
        