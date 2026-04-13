class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # dfs branch: if curr string is still palindrome (can check in O(1)?)
        res = []

        def is_palindrome(s: str):
            i = 0
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False

            return True

        def dfs(i, curr):
            if i >= len(s):
                if is_palindrome(curr[-1]):
                    res.append(curr[:])
                return

            if curr:
                curr[-1] += s[i]
                dfs(i + 1, curr)
                curr[-1] = curr[-1][:-1]

                if not is_palindrome(curr[-1]):
                    # don't need to check new str branch if curr is not palindrome
                    return

            dfs(i + 1, curr + [s[i]])

        dfs(0, [])
        return res
            

        