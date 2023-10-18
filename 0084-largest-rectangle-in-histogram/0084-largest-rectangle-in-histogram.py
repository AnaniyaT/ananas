class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-float('inf'))
        
        stk = [-1]
        
        maxArea = 0
        for ind in range(len(heights)):
            cur = heights[ind]
            
            while heights[stk[-1]] > cur:
                last = stk.pop()
                area = (ind - stk[-1] - 1) * heights[last]
                maxArea = max(maxArea, area)
            
            stk.append(ind)
            
        return maxArea
        