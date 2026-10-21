class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, remaining):
            if not remaining:
                res.append(curr.copy())
                return

            remaining_copy = remaining.copy()
            for n in remaining_copy:
                curr.append(n)
                remaining.discard(n)
                dfs(curr, remaining)
                curr.pop()
                remaining.add(n)

        dfs([], set(nums))
        return res

                    