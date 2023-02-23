class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        subArrays = 0
        runSum = 0
        count[0] += 1
        
        for num in nums:
            runSum += num
            target = runSum - k
            subArrays += count[target]
            count[runSum] += 1
            
        return subArrays