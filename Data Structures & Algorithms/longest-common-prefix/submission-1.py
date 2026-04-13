class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["bat","bag","bank","band"]
        # idx  = 2
        # word = "g" starts from 2
        # char = t always char[idx] of first word
        # ans  = ba
        # edge case only one str
        if len(strs) == 1:
            return strs[0]

        # O(n * m) time O(1) space
        ans = ""
        # iterate over an index up to max length of first word
        for idx in range(len(strs[0])):
            if idx >= len(strs[0]):
                return ans
            charFirst = strs[0][idx]
            # iterate over each word at index i
            for j in range(1, len(strs)):
                if idx >= len(strs[j]):
                    return ans                
                # if any word is different than the 1st word at idx return ans
                if strs[j][idx] != charFirst:
                    return ans
            # update ans
            ans += charFirst
        return ans
                    
