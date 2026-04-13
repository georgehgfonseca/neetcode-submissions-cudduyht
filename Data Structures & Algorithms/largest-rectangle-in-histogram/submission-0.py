class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque() # (index, height)
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                (topIdx, topHeight) = stack.pop()
                maxArea = max(maxArea, topHeight * (i - topIdx))
                start = topIdx
            stack.append((start, heights[i]))
        
        while stack:
            # compute heights that extend from its index all the way through the end
            (topIdx, topHeight) = stack.pop()
            area = topHeight * (len(heights) - topIdx)
            maxArea = max(maxArea, area)
            
        return maxArea