class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp = dict()
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return True
            anyMatch = False
            for word in wordDict:
                # try to match word and advance i
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    if dfs(i + len(word)):
                        anyMatch = True
            dp[i] = anyMatch
            return anyMatch

        return dfs(0)