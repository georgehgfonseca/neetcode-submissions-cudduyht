class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = dict()
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        
        for char in t:
            if char not in charCount or charCount[char] == 0:
                return False
            charCount[char] -= 1
        
        return True