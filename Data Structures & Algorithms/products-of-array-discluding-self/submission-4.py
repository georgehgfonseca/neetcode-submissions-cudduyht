class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
            
        prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] * num)
        sulfix = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                sulfix.append(nums[i])
            else:
                sulfix.insert(0, sulfix[0] * nums[i])
        print(prefix, sulfix)

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(1 * sulfix[i + 1])
            elif i == len(nums) - 1:
                ans.append(1 * prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * sulfix[i + 1])
        
        return ans

        