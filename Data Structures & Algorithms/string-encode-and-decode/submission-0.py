class Solution:

    def encode(self, strs: List[str]) -> str:
        # add some prefix to each string with the number of chars of each str
        # ["neet","code","love","you"] -> \4\neet\4\code\4\love\3\you
        output = ""
        for str in strs:
            output += f"|{len(str)}|{str}"
        return output


    def decode(self, s: str) -> List[str]:
        # read a char, if it is the marker, read the number n, then the ending marker, then n chars of the string
        output = []
        i = 0
        while i < len(s):
            if s[i] == "|":
                i += 1
                currNumStr = ""
                while s[i] != "|":
                    currNumStr += s[i]
                    i += 1
                currNum = int(currNumStr)
                output.append(s[i + 1:i + currNum + 1])
                i += currNum
            i += 1
        return output
