from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dfs(i, player, M):
            if i >= len(piles):
                return 0
            
            stones = 0
            best = 0 if player ==  "A" else float("inf")
            for X in range(i, min(i + (2 * M), len(piles))):
                stones += piles[X]
                if player == "A":
                    best = max(best, stones + dfs(X + 1, "B", max(M, X + 1 - i)))
                elif player == "B":
                    best = min(best, dfs(X + 1, "A", max(M, X + 1 - i)))
            
            return best

        return dfs(0, "A", 1)