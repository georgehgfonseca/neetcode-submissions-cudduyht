class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k               = 3
        # nums            = [1, 2, 3, 1]
        # i               =           *
        # set             = {1, 2, 3}
        # a set to compute element in range k
        numsInRange = set()
        if len(nums) <= k:
            return len(nums) != len(set(nums))
        
        for i in range(k):
            if nums[i] in numsInRange:
                return True
            numsInRange.add(nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] in numsInRange:
                return True
            numsInRange.discard(nums[i - k])
            numsInRange.add(nums[i])

        return False
            