# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot, isSubRoot):
            if not root:
                if subRoot:
                    return False
                return True
            
            if not subRoot:
                return False

            if root.val != subRoot.val:
                if not isSubRoot:
                    return False
                return dfs(root.left, subRoot, True) or dfs(root.right, subRoot, True)  

            return (dfs(root.left, subRoot.left, False) and dfs(root.right, subRoot.right, False)) or dfs(root.left, subRoot, True) or dfs(root.right, subRoot, True)  

        return dfs(root, subRoot, True)
        