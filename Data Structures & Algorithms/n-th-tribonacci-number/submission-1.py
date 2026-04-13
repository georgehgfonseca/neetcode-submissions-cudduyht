from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = deque([0, 1, 1])
        # 2 -> -1
        # 1 -> -2
        # 0 -> -3
        if n < 3:
            return dp[n - 3]
        for i in range(3, n + 1):
            dp.append(dp[-1] + dp[-2] + dp[-3])
            dp.popleft()
        return dp[-1]
        
    def tribonacci2(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            dp[i] = dp[i -1] + dp[i - 2] + dp[i - 3]
        return dp[n]
        