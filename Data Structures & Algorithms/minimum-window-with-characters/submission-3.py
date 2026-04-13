class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hasmap to store char count of t
        # two pointers - move right when all chars are not covered, move left while are covered (to recude substring)
        # t     = "ABC"
        # tChar = {'A': 1, 'B': 1, 'C': 1}
        # s     = "ADOBECODEBANC"
        # l, r  =            *  *
        # res   =       *       *
        if len(t) > len(s):
            return ""

        tCharCount = Counter(t)
        l, r = 0, len(t)
        currCharCount = Counter(s[l:r])
        res = float("inf")
        minL, minR = -1, -1

        def checkHasAllChars(curr, target): # O(26)
            for char in target:
                if char not in curr or curr[char] < target[char]:
                    return False
            return True
                        
        while r <= len(s):
            while checkHasAllChars(currCharCount, tCharCount):
                if r - l < res:
                    res = r - l
                    minL, minR = l, r

                currCharCount[s[l]] -= 1
                l += 1
            
            if r >= len(s):
                break

            currCharCount[s[r]] = currCharCount.get(s[r], 0)
            currCharCount[s[r]] += 1
            r += 1

        return s[minL: minR]



            



        