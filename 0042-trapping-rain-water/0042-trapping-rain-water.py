class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0 for _ in range(n)]
        maxRight = [0 for _ in range(n)]
        
        for ind in range(n):
            maxLeft[ind] = max(maxLeft[ind-1], height[ind])
        for ind in range(n):
            maxRight[~ind] = max(maxRight[~(ind-1)], height[~ind])
        
        # print(maxLeft)
        # print(maxRight)
        water = 0
        for ind in range(n):
            water += min(maxLeft[ind], maxRight[ind]) - height[ind]
        
        
        return water