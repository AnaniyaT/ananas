class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmx = rightmx = 0
        water = 0
        while l <= r:
            leftmx = max(height[l], leftmx)
            rightmx = max(rightmx, height[r])
            
            if leftmx < rightmx:
                water += leftmx - height[l]
                l += 1
            else:
                water += rightmx - height[r]
                r -= 1
        
        return water