class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')
        currSum = 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(minLen, r-l+1)
                currSum -= nums[l]
                l += 1
        
        if minLen == float('inf'):
            return 0
        else:
            return minLen