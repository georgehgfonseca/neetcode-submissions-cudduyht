class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        ansIdx = [0, 1]
        for i in range(len(s)):
            j = 1
            currAns = 1
            # odd lenght
            while i - j >= 0 and i + j < len(s):
                if s[i - j] != s[i + j]:
                    break
                currAns += 2
                if currAns > ans:
                    ans = currAns
                    ansIdx = [i - j, i + j + 1]
                j += 1
            # even lenght to right
            if i + 1 < len(s) and s[i] == s[i + 1]:
                currAns = 2
                if currAns > ans:
                    ans = currAns
                    ansIdx = [i, i + 2]
                j = 1
                while i - j >= 0 and i + 1 + j < len(s):
                    if s[i - j] != s[i + 1 + j]:
                        break
                    currAns += 2
                    if currAns > ans:
                        ans = currAns
                        ansIdx = [i - j, i + 1 + j + 1]
                    j += 1
        return s[ansIdx[0]:ansIdx[1]]



        