class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        dp = {}
        
        @cache
        def getMaxLen(num):
            if num in dp:
                return dp[num]
            
            if num not in numSet:
                return 0
            
            ans = 1 + getMaxLen(num-1)
            dp[num] = ans
            
            return ans
            
        for num in nums:
            getMaxLen(num)
            
        return max(dp.values())