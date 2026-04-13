# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root):
            if not root.left and not root.right:
                self.res = max(self.res, root.val)
                return root.val
            
            leftSum = dfs(root.left) if root.left else 0
            rightSum = dfs(root.right) if root.right else 0
            nodeSum = max(root.val, root.val + leftSum + rightSum, root.val + leftSum, root.val + rightSum)
            self.res = max(self.res, nodeSum)
            return max(root.val, root.val + leftSum, root.val + rightSum)
        
        dfs(root)
        return self.res
        