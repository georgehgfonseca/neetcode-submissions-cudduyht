class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums and explore some logic related to the limit, shifiting the right pointer to the left

        # store a hashmap of complement and pairs to form it: complement: ((i, j), ...) O(n^2)
        complementPairs = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = (nums[j] + nums[i]) * -1
                if complement not in complementPairs:
                    complementPairs[complement] = set()
                complementPairs[complement].add((i, j))
        
        print(complementPairs)
        triplets = []
        # iterate over each element and search it in the complement hashmap
        for k in range(len(nums)):
            if nums[k] in complementPairs:
                for (i, j) in complementPairs[nums[k]]:
                    if i != k and j != k:
                        triplets.append(sorted([nums[i], nums[j], nums[k]]))

        ans = []
        # filter duplicated triplets
        for triplet in triplets:
            if triplet not in ans:
                ans.append(triplet)
        return ans
        