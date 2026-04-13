class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixSum count
        # nums              = [-1, -1, 1]
        # i                 =   *
        # prefixCount       = {0: 1, -1: 1}
        # sum               = -1
        # res               = 0
        prefixCount = {0: 1}
        sum = 0
        res = 0
        for num in nums:
            sum += num
            targetDiff = sum - k
            if targetDiff in prefixCount:
                res += prefixCount[targetDiff]
            prefixCount[sum] = prefixCount.get(sum, 0) + 1
        return res
        # brute force
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res
        # two pointers
        # iterate over the array
        # while curSum is less than k, add elem
        # if curSum == k increase res
        # if curSum > k, move left pointer
        # nums          = [2, -1, 1, 2]
        # l, r          = ||
        l, r = 0, 0
        curSum = 0
        res = 0
        while r < len(nums):
            if curSum == k:
                res += 1
                if l < r:
                    r += 1
                else:
                    l += 1
                curSum += nums[r]
            if curSum > k:
                curSum -= nums[l]
                l += 1
            else:
                r += 1
                curSum += nums[r]
        return res
