# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if root1.val != root2.val:
                return False
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
            
        
        def helper(root, subRoot):
            if not root and subRoot:
                return False
            if isSameTree(root, subRoot):
                return True

            return helper(root.left, subRoot) or helper(root.right, subRoot) 
        
        return helper(root, subRoot)
            