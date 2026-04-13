class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        for i in range(len(s)):
            l, r = i, i
            # try to grow to the left and to the right (odd case)
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        
        for i in range(len(s) - 1):
            l, r = i, i + 1
            # try to grow to the left and to the right (even case)
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        
        return res

    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True

    def longestPalindromeTL(self, s: str) -> str:
        # brute force
        res = 0
        maxSubstr = ""
        for start in range(len(s)):
            for end in range(start, len(s)):
                substr = s[start: end + 1]
                if self.isPalindrome(substr):
                    if end + 1 - start > res:
                        res = end + 1 - start
                        maxSubstr = substr
        return maxSubstr