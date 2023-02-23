class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] += 1
        runSum = 0
        subarrays = 0
        
        for num in nums:
            runSum += num
            mod = runSum%k
            subarrays += count[mod]
            count[mod] += 1
        
        return subarrays