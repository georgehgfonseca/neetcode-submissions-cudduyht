class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitChar = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
        }

        def dfs(i, curr):
            if i >= len(digits):
                if curr:
                    res.append(curr)
                return

            for char in digitChar[digits[i]]:
                dfs(i + 1, curr + char)

        dfs(0, "")
        return res
