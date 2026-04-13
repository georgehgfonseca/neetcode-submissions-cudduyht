class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combs = []
        nums = [i + 1 for i in range(n)]

        # for each idx you can either add nums[idx] to currComb or not
        def helper(idx, currComb):
            if len(currComb) == k:
                combs.append(currComb)
                return

            if idx >= len(nums):
                return
            
            helper(idx + 1, currComb[:])
            helper(idx + 1, currComb[:] + [nums[idx]])

        helper(0, [])
        return combs