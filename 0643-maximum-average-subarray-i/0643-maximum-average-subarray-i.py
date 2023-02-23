class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum
        
        for r in range(k, len(nums)):
            currSum += nums[r]
            currSum -= nums[r-k]
            
            maxSum = max(maxSum, currSum)
            
        return maxSum/k