class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        diff = float('inf')
        l = 0
        
        nums.sort()
        for r in range(max(n-4, 0), n):
            diff = min(diff, nums[r] - nums[l])
            l += 1
            
        if diff == float('inf'):
            return 0
        
        return diff
            
            