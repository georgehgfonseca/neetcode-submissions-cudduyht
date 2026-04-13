class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            ans += 1
            offset = 1
            while i - offset >= 0 and i + offset < len(s):
                if s[i - offset] != s[i + offset]:
                    break
                ans += 1
                offset += 1

            if i + 1 < len(s) and s[i] == s[i + 1]:
                ans += 1
                offset = 1
                while i - offset >= 0 and i + 1 + offset < len(s):
                    if s[i - offset] != s[i + 1 + offset]:
                        break
                    ans += 1
                    offset += 1
        return ans