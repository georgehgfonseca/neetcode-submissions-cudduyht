class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = dict()
        dp[len(s)] = 1

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                # can be decoded 2 ways
                print(f"2-way i={i}")
                dp[i] = dfs(i + 1) + dfs(i + 2)
                return dp[i]
            dp[i] = dfs(i + 1)
            return dp[i]
        
        dfs(0)
        print(dp)
        return dp[0]
        