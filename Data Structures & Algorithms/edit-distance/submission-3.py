class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)

        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j >= len(word2):
                return len(word1) - i
            
            if i >= len(word1):
                return len(word2) - j

            res = None
            if word1[i] == word2[j]:
                # can be greedy?
                res = dfs(i + 1, j + 1)
            else:
                # either replace char, delete char, or insert char
                res = 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)

    def minDistance2(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)

        def dfs(i, j):
            if j >= len(word2):
                return len(word1) - i
            
            if i >= len(word1):
                return len(word2) - j

            if word1[i] == word2[j]:
                # can be greedy?
                return dfs(i + 1, j + 1)
            
            # requires a fix
            # either replace char, delete char, or insert char
            return min(1 + dfs(i + 1, j + 1), 1 + dfs(i + 1, j), 1 + dfs(i, j + 1))
        
        return dfs(0, 0)
