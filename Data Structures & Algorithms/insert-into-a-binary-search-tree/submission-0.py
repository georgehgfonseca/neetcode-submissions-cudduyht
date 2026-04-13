# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # navigate to the postion
        if not root:
            return TreeNode(val)

        head = root
        insert, prev = "L", root
        while root:
            if root.val > val:
                insert, prev = "L", root
                root = root.left
            else:
                insert, prev = "R", root
                root = root.right
        
        if insert == "L":
            prev.left = TreeNode(val)
        if insert == "R":
            prev.right = TreeNode(val)
        
        return head
