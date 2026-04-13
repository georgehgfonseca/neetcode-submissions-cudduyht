from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(i):
            if i >= len(s):
                return True

            for word in wordDict:
                n = len(word)
                if i + n > len(s):
                    continue

                if s[i:i+n] == word:
                    if dfs(i + n):
                        return True
            return False

        return dfs(0)
        