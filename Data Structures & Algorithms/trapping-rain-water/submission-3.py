class Solution:
    def trap(self, height: List[int]) -> int:
        # sum all trappedWatter
        # for each bar, compute and store the maximum bar at its left and at its right
        left = [height[0]]
        maxLeft = height[0]
        for i in range(1, len(height)):
            if height[i] > maxLeft:
                maxLeft = height[i]
            left.append(maxLeft)
        right = [height[-1]]
        maxRight = height[-1]
        for i in range(len(height) -2, -1, -1):
            if height[i] > maxRight:
                maxRight = height[i]
            right.insert(0, maxRight)
        
        # the trappedWater in the i-th bar is min(left[i], right[i]) - height[i]
        print(left)
        print(right)
        ans = 0
        for i in range(1, len(height) - 1):
            trapperWater = min(left[i], right[i]) - height[i]
            ans += trapperWater
        return ans


        # height           = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        # l                = 7
        # r                = 8
        # trappedBars      = 0
        # trappedBarsHeight= 0
        # ans              = 5
        l = 0
        r = 1
        trappedBars = 0
        trappedHeight = 0
        ans = 0
        while r < len(height):
            if height[l] < height[r]:
                # cannot trap more watter
                trappedWater = (min(height[l], height[r]) * trappedBars) - trappedHeight
                ans += trappedWater
                trappedBars = 0
                trappedHeight = 0
                l = r
                r += 1
            else:
                # trapping water
                trappedBars += 1
                trappedHeight += height[r]
                r += 1
        return ans


        # sliding window starting at l = 0 and r = 1
        # keep track of intermediate heights
        # if r >= l, 
        #     sum ans with trapped water ((min(heights[l], heights[r]) * trappedBars) - trappedHeights)
        #     set trappedBars to 0, trappedHeights to 0, and move l to r and r to r + 1
        # else (r < l) increase trappedBars += 1, trappedHeights += height[r], r += 1 



        # sliding window starting at l = 0 and r = 2
        # move to r + 1 if >= than r
        # if smaller or equal, calculate the water between l and r, and move l to r and r to r + 2
        # when calculating the water, subtract the height of bars between l and r

        # two pointers, one at the beginning l = 0, other at the end r = len(height) - 1
        # move the smallest height between height[l] and height[r]