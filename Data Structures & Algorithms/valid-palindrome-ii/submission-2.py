class Solution:
    def validPalindrome(self, s: str) -> bool:
        # s         = acdccba
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True

        # brute force
        def  isPalindrome(s: str):
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True
        
        # check the original str too
        if isPalindrome(s):
            return True
        
        # iterate over each char
        for i in range(len(s)):
            # check if resulting when removing it is true
            if isPalindrome(s[:i] + s[i + 1:]):
                return True
        return False