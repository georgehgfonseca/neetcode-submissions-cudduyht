class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(int(len(s) / 2)):
                if s[i] != s[-i -1]:
                    return False
            return True
        
        res = []
        def helper(idx, currSet):
            if idx == len(s) - 1:
                # a full split is reached
                for str in currSet:
                    if not isPalindrome(str):
                        return
                res.append(currSet)
                return
        
            prevCharCount = 0
            for i in range(len(currSet) - 1):
                prevCharCount += len(currSet[i])
            splitSet = currSet[:-1] + [currSet[-1][:idx + 1 - prevCharCount]] + [currSet[-1][idx + 1 - prevCharCount:]]
            if len(splitSet) < 2 or isPalindrome(splitSet[-2]):
                helper(idx + 1, splitSet)
            helper(idx + 1, currSet)

        helper(0, [s])
        return res