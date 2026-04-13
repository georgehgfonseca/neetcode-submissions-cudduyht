class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        dp = dict()

        def dfs(idxs):
            key = frozenset(idxs)
            if not key:
                return 0
            if key in dp:
                return dp[key]

            maxSum = float("-inf")
            for idx in key:
                # find closest left and right neighbors
                left = -1
                for leftCand in key:
                    if left < leftCand < idx:
                        left = leftCand
                right = len(nums)
                for rightCand in key:
                    if idx < rightCand < right:
                        right = rightCand

                leftMult = 1 if left == -1 else nums[left]
                rightMult = 1 if right == len(nums) else nums[right]

                newIdxs = set(key)
                newIdxs.remove(idx)

                total = dfs(newIdxs) + (leftMult * nums[idx] * rightMult)
                maxSum = max(maxSum, total)

            dp[key] = maxSum
            return maxSum
        
        idxs = {i for i in range(len(nums))}
        return dfs(idxs)

    def maxCoins3(self, nums: List[int]) -> int:

        def dfs(arr, currSum):
            if len(arr) == 0:
                return currSum
            
            maxSum = float("-inf")
            childrenSums = []
            for i in range(len(arr)):
                left = 1 if i - 1 < 0 else arr[i - 1]
                right = 1 if i + 1 == len(arr) else arr[i + 1]
                newArr = arr.copy()
                newArr.pop(i)
                newSum = currSum + (left * arr[i] * right)
                childrenSums.append(dfs(newArr, newSum))
            return max(childrenSums)
        
        return dfs(nums, 0)
                

    def maxCoins2(self, nums: List[int]) -> int:
        self.res = 0
        def dfs(arr, currSum):
            if len(arr) == 0:
                self.res = max(self.res, currSum)
                return
            
            for i in range(len(arr)):
                left = 1 if i - 1 < 0 else nums[i - 1]
                right = 1 if i + 1 == len(arr) else nums[i + 1]
                newArr = arr.copy()
                newArr.pop(i)
                dfs(newArr, currSum + (left * nums[i] * right))
        
        dfs(nums, 0)
        return self.res
                

        