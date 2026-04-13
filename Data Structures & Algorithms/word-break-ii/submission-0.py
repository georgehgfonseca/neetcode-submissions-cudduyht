from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)
        res = []

        def dfs(i, curr):
            print(i, curr)
            if i >= len(s):
                res.append(" ".join(curr))
                return

            for word in wordDict:
                n = len(word)
                if i + n > len(s):
                    continue

                if s[i:i+n] == word:
                    curr.append(word)
                    dfs(i + n, curr)
                    curr.pop()

        dfs(0, [])
        return res