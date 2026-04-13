class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, wordIdx):
            if wordIdx >= len(word):
                return True
            
            out_of_bounds = i < 0 or j < 0 or i >= len(board) or j >= len(board[i])
            if out_of_bounds or board[i][j] != word[wordIdx] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            res = dfs(i + 1, j, wordIdx + 1) or dfs(i - 1, j, wordIdx + 1) or dfs(i, j + 1, wordIdx + 1) or dfs(i, j - 1, wordIdx + 1) 
            visited.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                if dfs(i, j, 0):
                    return True

        return False

        