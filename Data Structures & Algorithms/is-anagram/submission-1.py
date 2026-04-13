class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_count = dict()
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        for letter in t:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            else:
                letter_count[letter] -= 1
        return True