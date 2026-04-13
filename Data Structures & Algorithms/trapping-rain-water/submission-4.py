class Solution:
    def trap(self, height: List[int]) -> int:
        # for each cell calc the larger on its left and larger on its right
        # the traped water at i index is min(left[i], right[i]) - height[i] 
        # negative can be dismissed
        largestLeft = [0]
        for i in range(1, len(height)):
            largestLeft.append(max(height[i - 1], largestLeft[-1]))

        largestRight = [0]
        for i in range(len(height) - 2, -1, -1):
            largestRight.append(max(height[i + 1], largestRight[-1]))
        largestRight.reverse()

        res = 0
        for i in range(1, len(height) - 1):
            trapped = min(largestLeft[i], largestRight[i]) - height[i]
            if trapped > 0:
                res += trapped

        return res
