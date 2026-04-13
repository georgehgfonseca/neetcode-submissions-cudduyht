class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s       = "pwwkew"
        # l,i     =     * *
        # seen    = {wke}
        seenChars = set()
        res = 0
        i, l = 0, 0
        while i < len(s):
            if s[i] not in seenChars:
                seenChars.add(s[i])
                res = max(res, len(seenChars))
            else:
                while l < len(s) and s[l] != s[i]:
                    seenChars.discard(s[l])
                    l += 1
                while l < len(s) and s[l] == s[i]:
                    l += 1
            i += 1
        return res
        