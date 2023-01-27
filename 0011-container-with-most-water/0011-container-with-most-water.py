class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        currMax = 0
        while l < r:
            curr = min(height[l],height[r])*(r-l)
            currMax = max(currMax,curr)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return currMax