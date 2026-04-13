class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(i, j):
            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0

            if s[i] != t[j]:
                return dfs(i + 1, j)

            # can either use i to move j or not
            return dfs(i + 1, j + 1) + dfs(i + 1, j)
        
        return dfs(0, 0)
        