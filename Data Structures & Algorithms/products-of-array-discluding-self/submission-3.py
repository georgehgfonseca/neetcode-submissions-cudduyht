class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        overallProduct = 1
        zeroIdxs = set()
        for i, num in enumerate(nums):
            if num == 0:
                zeroIdxs.add(i)
                continue
            overallProduct *= num

        if len(zeroIdxs) > 1:
            # For edge cases such as [0, 8, 0] and [0, 0]
            return [0] * len(nums)

        ans = []
        for i, num in enumerate(nums):
            if num == 0:
                ans.append(overallProduct)
            elif zeroIdxs:
                ans.append(0)
            else:
                ans.append(int(overallProduct / num))
        return ans

        