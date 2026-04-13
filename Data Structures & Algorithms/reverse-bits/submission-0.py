class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # take the i-th bit (right to left)
            bit = n & 1 # n % 2 would work too
            n >>= 1
            if bit:
                res += 2 ** (31 - i)
        return res

