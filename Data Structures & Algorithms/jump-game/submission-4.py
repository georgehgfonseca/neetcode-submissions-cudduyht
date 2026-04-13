class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums  = [1, 2, 0, 1, 0]
        # can   = [True, True, True, True, False]
        # stack = [2]
        # i     = 3
        # j     = 4 
        # use a stack to handle open positions for jumping
        # update que stack and the can array when evaluating a position
        # O(n2) (?)
        if len(nums) == 1:
            return True
        canJump = [False for _ in nums]
        canJump[0] = True
        stack = [0]
        while stack:
            i = stack.pop()
            for j in range(i + 1, i + 1 + nums[i]):
                if j >= len(nums):
                    break
                if j == len(nums) - 1:
                    return True
                if not canJump[j]:
                    canJump[j] = True
                    stack.append(j)
        return False


