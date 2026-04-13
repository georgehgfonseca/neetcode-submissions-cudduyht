class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                curr = res[i + j] + (int(num1[i]) * int(num2[j]))
                carry = curr // 10
                res[i + j] = curr % 10
                res[i + j + 1] += carry

        res = res[::-1]
        strRes = [str(digit) for digit in res]

        strRes = "".join(strRes)
        return strRes.lstrip("0")