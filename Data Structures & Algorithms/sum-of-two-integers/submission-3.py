class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        i = 0
        while a or b:
            bitA = a & 1
            bitB = b & 1
            a >>= 1
            b >>= 1
            if bitA and bitB:
                res += 2 ** (i + 1)
            elif bitA or bitB:
                res += 2 ** i
            i += 1
        return res
        
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)