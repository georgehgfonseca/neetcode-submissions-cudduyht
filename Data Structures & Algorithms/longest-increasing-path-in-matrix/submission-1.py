class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = dict()
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            cands = set()
            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                cands.add((i + 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                cands.add((i, j + 1))
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                cands.add((i - 1, j))
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                cands.add((i, j - 1))
            
            if not cands:
                return 0
            
            best = 0
            for cand in cands:
                best = max(best, 1 + dfs(cand[0], cand[1]))
            
            dp[(i, j)] = best
            return best

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, 1 + dfs(i, j))

        return res

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j):
            cands = set()
            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                cands.add((i + 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                cands.add((i, j + 1))
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                cands.add((i - 1, j))
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                cands.add((i, j - 1))
            
            if not cands:
                return 0
            
            best = 0
            for cand in cands:
                best = max(best, 1 + dfs(cand[0], cand[1]))
            
            return best

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, 1 + dfs(i, j))

        return res


