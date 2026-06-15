# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs tracking the max val in path
        def dfs(node, max_val):
            if not node:
                return 0

            curr_node = 0
            if node.val >= max_val:
                curr_node = 1

            max_val = max(node.val, max_val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            return curr_node + left + right

        return dfs(root, float("-inf"))

