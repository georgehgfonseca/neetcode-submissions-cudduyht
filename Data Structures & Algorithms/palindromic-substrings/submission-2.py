class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1
            
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1
        return res

    def countSubstrings2(self, s: str) -> int:
        palindromeIdxs = set()
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                # to avoid duplicates
                if (l, r + 1) not in palindromeIdxs:
                    palindromeIdxs.add((l, r + 1))
                l -= 1
                r += 1
            
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                # to avoid duplicates
                if (l, r + 1) not in palindromeIdxs:
                    palindromeIdxs.add((l, r + 1))
                l -= 1
                r += 1
        return len(palindromeIdxs)
            
                
        