class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, subset):
            if i == len(nums):
                print(f"1) {i} - return {len(subset)}")
                return len(subset)
            # if not subset or nums[i] < subset[0]:
            if not subset:
                print(f"2) {i} - {subset} add {nums[i]}")
                return dfs(i + 1, [nums[i]])
            
            if nums[i] > subset[-1]:
                print(f"3) {i} - {subset} add {nums[i]}")
                return dfs(i + 1, subset[:] + [nums[i]])
            else:
                reducedSubset = subset[:]
                while reducedSubset and reducedSubset[-1] >= nums[i]:
                    reducedSubset.pop()
                print(f"4) {i} - max({subset}, {reducedSubset + [nums[i]]}) ")
                return max(dfs(i + 1, subset[:]), dfs(i + 1, reducedSubset + [nums[i]]))
        
        return dfs(0, [])


    def lengthOfLIS2(self, nums: List[int]) -> int:
        # brute force
        l, r = 0, 0
        res = 0
        stack = []
        # nums              = [0, 1, 0, 3, 2, 3]
        # l, r              =  *     *
        # stack             = [0, 1]
        while r < len(nums):
            while r < len(nums) and nums[r] >= nums[l]:
                if stack and stack[0] == nums[r]:
                    r += 1
                    continue
                while stack and stack[-1] >= nums[r]:
                    #print("pop  ", l, r, stack)
                    elem = stack.pop()
                stack.append(nums[r])
                #print("push ", l, r, stack)
                res = max(res, len(stack))
                r += 1
            print(l, r, stack)
            stack = []
            l = r
        return res