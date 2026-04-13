class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i, j):
            if (j >= len(p) and i >= len(s)) or (j == len(p) - 2 and p[j + 1] == "*" and i >= len(s)):
                return True
            if i >= len(s) or j >= len(p):
                return False
            
            if j + 1 < len(p) and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    return dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    return dfs(i, j + 2)
            elif s[i] == p[j] or p[j] == ".":
                return dfs(i + 1, j + 1)
            else:
                return False
        
        return dfs(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:

        def dfs(i, j):
            if j >= len(p) and i >= len(s):
                return True
            if i >= len(s) or j >= len(p):
                return False
            
            if s[i] == p[j] or p[j] == ".":
                return dfs(i + 1, j + 1)
            elif p[j] == "*":
                # can either jump a char on i or not
                return dfs(i + 1, j) or dfs(i + 1, j + 1)
            else:
                return False
        
        return dfs(0, 0)



            
        