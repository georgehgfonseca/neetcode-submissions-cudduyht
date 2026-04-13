class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)] # (height, index)
        res = heights[0]
        for i in range(1, len(heights)):
            start = i
            print(stack, res)
            while stack and heights[i] < stack[-1][0]:
                prevHeight, prevI = stack.pop()
                res = max(res, prevHeight * (i - prevI))
                start = prevI
            
            stack.append((heights[i], start))

        while stack:
            height, index = stack.pop()
            res = max(res, height * (len(heights) - index))
        
        return res


        