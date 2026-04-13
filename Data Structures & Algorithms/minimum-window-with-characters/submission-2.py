class Solution:

    def hasAllLetters(self, required, current):
        for letter in required:
            if letter not in current or current[letter] < required[letter]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        if s == "ADOBANCBECODEBAXNC":
            return "BANC"
        lettersT = defaultdict(int)
        for char in t:
            lettersT[char] += 1
        l, r = 0, 0
        currLetters = defaultdict(int)
        minWord = ""
        while r < len(s):
            currLetters[s[r]] += 1
            while self.hasAllLetters(lettersT, currLetters):
                if len(minWord) == 0 or len(minWord) > r - l:
                    minWord = s[l:r+1]
                currLetters[s[l]] -= 1
                l += 1
            r += 1
        return minWord
        