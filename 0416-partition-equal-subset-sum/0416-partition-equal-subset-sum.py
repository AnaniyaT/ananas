class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        if total % 2:
            return False
        
        half = total // 2
        
        @cache
        def dp(ind, req):
            if req < 0 or ind >= n :
                return False
            
            if not req:
                return True
            
            return dp(ind + 1, req - nums[ind]) or dp(ind + 1, req)
        
        return dp(0, half)