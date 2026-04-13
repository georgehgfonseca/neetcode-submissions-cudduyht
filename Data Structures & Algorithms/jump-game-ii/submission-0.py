class Solution:
    def jump(self, nums: List[int]) -> int:
        # nums   = [2, 1, 2, 1, 0]
        # i      = 2
        # ans    = 2
        # maxVal = -1
        # maxIdx = -1
        # j      = 3 4
        ans = 0
        i = 0
        while i < len(nums) - 1:
            ans += 1
            # evaluate next move
            maxIdx = -1
            maxVal = -1
            for j in range(i + 1, i + 1 + nums[i]):
                if j >= len(nums) - 1:
                    return ans
                if nums[j] + j > maxVal:
                    maxVal = nums[j] + j
                    maxIdx = j
            # if maxIdx == -1:
            #    return False
            i = maxIdx

        return ans
