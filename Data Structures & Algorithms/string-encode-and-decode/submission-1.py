class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "|" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        charsStr = ""
        i = 0
        while i < len(s):
            if s[i] != "|":
                charsStr += s[i]
            else:
                chars = int(charsStr)
                res.append(s[i + 1: i + 1 + chars])
                charsStr = ""
                i += chars
            i += 1
        return res

