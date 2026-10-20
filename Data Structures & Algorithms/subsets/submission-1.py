class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def dfs(i, curr):
            if i >= n:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])
        return res
        