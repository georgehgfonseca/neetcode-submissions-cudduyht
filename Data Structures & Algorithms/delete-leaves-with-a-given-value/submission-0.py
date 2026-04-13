# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root, parent, isLeftChild):
            if not root:
                return
            if not root.left and not root.right:
                if root.val == target:
                    if parent.val == target:
                        self.mustCheckLeaves = True
                    if isLeftChild:
                        parent.left = None
                    else:
                        parent.right = None
                return
            
            dfs(root.left, root, True)
            dfs(root.right, root, False)
        
        if not root:
            return root
        
        self.mustCheckLeaves = True
        while self.mustCheckLeaves:
            self.mustCheckLeaves = False
            if not root.left and not root.right and root.val == target:
                return None
            dfs(root.left, root, True)
            dfs(root.right, root, False)
        
        return root

