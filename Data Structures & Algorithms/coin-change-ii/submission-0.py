class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = dict()

        def dfs(i, sum):
            if (i, sum) in dp:
                return dp[(i, sum)]

            if i >= len(coins) or sum > amount:
                return 0

            if sum == amount:
                return 1
            
            # either add one more i-th coin or move to next
            dp[(i, sum)] = dfs(i, sum + coins[i]) + dfs(i + 1, sum)
            return dp[(i, sum)]

        return dfs(0, 0)

    def change2(self, amount: int, coins: List[int]) -> int:
        
        def dfs(i, sum):
            if i >= len(coins) or sum > amount:
                return 0

            if sum == amount:
                return 1
            
            # either add one more i-th coin or move to next
            return dfs(i, sum + coins[i]) + dfs(i + 1, sum)

        return dfs(0, 0)

            
            
