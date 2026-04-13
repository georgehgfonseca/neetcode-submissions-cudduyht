class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(s1) and j >= len(s2):
                return i + j == len(s3)
            
            res = None
            if i < len(s1) and j >= len(s2):
                # can only use s1
                if s1[i] != s3[i + j]:
                    res = False
                else:
                    res = dfs(i + 1, j)

            elif i >= len(s1) and j < len(s2):
                # can only use s2
                if s2[j] != s3[i + j]:
                    res = False
                else:
                    res = dfs(i, j + 1)

            else:
                # can use either a char from s1 or s2
                usingS1 = dfs(i + 1, j) if s1[i] == s3[i + j] else False
                usingS2 = dfs(i, j + 1) if s2[j] == s3[i + j] else False
                res = usingS1 or usingS2
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i >= len(s1) and j >= len(s2):
                return i + j == len(s3)
            
            if i < len(s1) and j >= len(s2):
                # can only use s1
                if s1[i] != s3[i + j]:
                    return False
                return dfs(i + 1, j)

            elif i >= len(s1) and j < len(s2):
                # can only use s2
                if s2[j] != s3[i + j]:
                    return False
                return dfs(i, j + 1)

            else:
                # can use either a char from s1 or s2
                usingS1 = dfs(i + 1, j) if s1[i] == s3[i + j] else False
                usingS2 = dfs(i, j + 1) if s2[j] == s3[i + j] else False
                return usingS1 or usingS2
        
        return dfs(0, 0)
        