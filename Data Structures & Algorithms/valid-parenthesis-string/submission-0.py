class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()

        def dfs(i, open):
            if (i, open) in dp:
                return dp[(i, open)]
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == "(":
                res = dfs(i + 1, open + 1)
            elif s[i] == ")":
                res = dfs(i + 1, open - 1)
            else:
                # adds a "(", ")", or " "
                res = dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)

            dp[(i, open)] = res
            return res
            
        return dfs(0, 0)

    def checkValidString2(self, s: str) -> bool:

        def dfs(i, open):
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == "(":
                return dfs(i + 1, open + 1)
            elif s[i] == ")":
                return dfs(i + 1, open - 1)
            else:
                # adds a "(", ")", or " "
                return dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)
        
        return dfs(0, 0)


    def checkValidString2(self, s: str) -> bool:
        # greedy: * will always be ) if any ( in stack - not really - need to check reamining string
        open = 0
        for letter in s:
            print(open, letter, end=" ")
            if letter == "(":
                open += 1
            elif letter == ")":
                if open == 0:
                    return False
                open -= 1
            else:
                if open > 0:
                    open -= 1
            print(open)

        return open == 0
                

        