class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
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