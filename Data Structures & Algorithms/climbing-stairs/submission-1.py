class Solution:
    def climbStairs(self, n: int) -> int:
        # store in DP in howmany ways I can get to degree x, calculate up until n
        dp = [1, 2]
        if n <= 2:
            return dp[n - 1]
        
        for i in range(2, n):
            dp.append(dp[-1] + dp[-2]) # from n-1 with 1 hop, from n-2 with 2 hop, and from n-2 with 1 hop of 2 steps
        
        return dp[-1]
        