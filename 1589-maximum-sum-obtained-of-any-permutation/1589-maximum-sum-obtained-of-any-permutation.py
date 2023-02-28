class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        timesAdded = [0]*(len(nums)+1)
        
        for start, end in requests:
            timesAdded[start] += 1
            timesAdded[end+1] -= 1
            
        timesAdded = sorted(accumulate(timesAdded), reverse=True)
        nums.sort(reverse=True)
        
        result = 0
        for ind in range(len(nums)):
            result += nums[ind]*timesAdded[ind]
            
        mod = 1000000007
            
        return result%mod
    