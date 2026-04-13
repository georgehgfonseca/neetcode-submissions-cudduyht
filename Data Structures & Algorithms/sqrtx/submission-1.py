class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        # x        = 8
        # l        = 2
        # r        = 3
        # m        = 2
        l, r = 0, x
        while l <= r:
            m = (r + l) // 2
            if m * m < x:
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
        if m * m > x:
            return m - 1
        return m
        