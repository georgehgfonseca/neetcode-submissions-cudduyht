# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        self.diameter = 0
        def helper(root):
            if not root:
                return
            
            currDiameter = height(root.left) + height(root.right)
            self.diameter = max(self.diameter, currDiameter)

            helper(root.left)
            helper(root.right)

        helper(root)

        return self.diameter


            
        