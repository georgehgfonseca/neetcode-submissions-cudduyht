class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            out_of_bounds = i < 0 or j < 0 or i >= m or j >= n
            if out_of_bounds:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)