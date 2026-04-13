# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        l, r = 1, n
        while l <= r:
            m = (r + l) // 2
            isLower = guess(m)
            if isLower == -1:
                r = m - 1
            elif isLower == 0:
                return m
            else:
                l = m + 1
