class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0

            res = None
            if s[i] != t[j]:
                res = dfs(i + 1, j)
            else:
                # can either use i to move j or not
                res = dfs(i + 1, j + 1) + dfs(i + 1, j)
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)

    def numDistinct2(self, s: str, t: str) -> int:

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
        