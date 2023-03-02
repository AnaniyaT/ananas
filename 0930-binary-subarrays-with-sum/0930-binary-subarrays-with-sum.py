class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        subArrays = 0
        
        runSum = 0
        for num in nums:
            runSum += num
            subArrays += count[runSum - goal]
            count[runSum] += 1
            
        return subArrays
            
        
        