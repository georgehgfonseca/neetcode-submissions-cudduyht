class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in pair:
                stack.append(char)
                continue

            if not stack:
                return False
            
            if stack[-1] == "(" and char != ")" or stack[-1] == "[" and char != "]" or stack[-1] == "{" and char != "}":
                return False

            stack.pop()

        return len(stack) == 0


        