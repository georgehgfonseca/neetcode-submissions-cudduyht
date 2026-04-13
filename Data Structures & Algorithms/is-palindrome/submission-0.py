class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess the string removing non-alphanumeric chars and making all letters to lower
        cleanS = ""
        for char in s:
            if not char.isalnum():
                continue
            cleanS += char.lower()
        
        # check if palindrome with two pointers
        for i in range(len(cleanS) // 2):
            if cleanS[i] != cleanS[-i - 1]:
                return False
        return True


        