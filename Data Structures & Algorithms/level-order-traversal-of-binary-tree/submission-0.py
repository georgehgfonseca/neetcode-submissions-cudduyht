# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do a dfs keeping track of the level
        res = []
        def dfs(root, level):
            if not root:
                return
            
            if len(res) < level:
                res.append([])
            
            res[level - 1].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 1)
        return res
            

        