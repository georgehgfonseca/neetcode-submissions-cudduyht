class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        # use two pointers, i = 0 and j = len(heights) - 1
        i = 0
        j = len(heights) - 1
        while i < j:
            # calculate water between i and j
            water = (j - i) * min(heights[i], heights[j])
            ans = max(ans, water)
            # shift the smaller height
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return ans

        # brute force iterate twice over the array
        # calculate the maximum water
        ans = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                water = (j - i) * min(heights[i], heights[j])
                ans = max(ans, water)
        return ans
        