class Solution:
    def numSquares(self, n: int) -> int:
        self.minRes = float("inf")
        dp = dict()

        def dfs(target):
            if target == 0:
                return 0
            if target in dp:
                return dp[target]
            
            res = target
            for i in range(1, target + 1):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))
            dp[target] = res
            return res

        return dfs(n)

    def numSquares3(self, n: int) -> int:
        self.minRes = float("inf")
        
        def dfs(i, currN, currRes):
            if currN == 0:
                self.minRes = min(self.minRes, currRes)
                return
            if i <= 0:
                return
            
            sq = math.sqrt(i)
            if int(sq) == sq:
                # can use perfect square or not
                dfs(currN - i, currN - i, currRes + 1)
            dfs(i - 1, currN, currRes)
        
        dfs(n, n, 0)

        return self.minRes
        
    def numSquares2(self, n: int) -> int:
        # decrease n by 1 and check if is a perfect square
        # sum them recursivelly, from largest to smallest
        # n            = 4
        # i            = 4
        # res          = 2
        i = n
        res = 0
        while i > 0:
            sq = math.sqrt(i)
            if int(sq) == sq:
                # can use perfect square or not
                res += 1
                n -= i
                i = n
            else:
                i -= 1
        return res

