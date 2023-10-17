class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        
        @cache
        def dfs(idx, isEven):
            if idx >= n:
                return 0
            
            if isEven:
                return max(dfs(idx + 1, False) + nums[idx], dfs(idx + 1, True))
            
            return max(dfs(idx + 1, True) - nums[idx], dfs(idx + 1, False))
        
        return dfs(0, True)