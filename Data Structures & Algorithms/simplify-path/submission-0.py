class Solution:
    def simplifyPath(self, path: str) -> str:
        # path          = "/..//_home/a/b/..///"
        # res           = 
        # if read / and not prev == / skip
        stack = []
        curr = ""

        for char in path + "/":
            if char == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                
                curr = ""
            
            else:
                curr += char

        return "/" + "/".join(stack)
                


