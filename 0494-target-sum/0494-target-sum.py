class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def rec(ind, tar):
            if ind < 0:
                return int(not tar)
            
            ways = 0
            
            ways += rec(ind-1, tar+nums[ind])
            ways += rec(ind-1, tar-nums[ind])
            
            return ways
        
        return rec(len(nums)-1, target)