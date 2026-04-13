class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                # can decode 2 ways
                return dfs(i + 1) + dfs(i + 2)
            return dfs(i + 1)
        
        return dfs(0)