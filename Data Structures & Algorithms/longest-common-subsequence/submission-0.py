class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = dict()
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(text1) or j >= len(text2):
                return 0

            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))

            dp[(i, j)] = res
            return res

        return dfs(0, 0)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)

            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)
