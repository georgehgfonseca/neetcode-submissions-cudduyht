class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get the minimum (and maximum) rate, increasing until can eat all bananas (binary search?)
        # min = ceil(sum(piles) / h)
        # max = max(piles)
        # how to (efficiently) check if can eat all with rate k? sum the ceiled divide of each pile by the rate? O(n)
        def canEat(piles, rate, h):
            res = 0
            for pile in piles:
                res += math.ceil(pile/rate)
                if res > h:
                    return False
            return True

        l, r = math.ceil(sum(piles) / h), max(piles)
        res = r
        while l <= r:
            m = (r + l) // 2
            if canEat(piles, m, h):
                res = min(res, m)
                # try with smaller rate (search left)
                r = m - 1
            else:
                l = m + 1
        
        return res