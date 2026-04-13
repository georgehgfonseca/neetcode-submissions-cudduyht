class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N = min(len(word1), len(word2))
        res = ""
        for i in range(N):
            res += word1[i]
            res += word2[i]
        
        if len(word1) > len(word2):
            res += word1[N:]
        else:
            res += word2[N:]
        return res

