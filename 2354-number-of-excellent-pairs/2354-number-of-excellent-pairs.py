class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def countSetBits(num):
            return Counter(bin(num))["1"]
        
        nums = list(set(nums))
        
        bitCounts = [countSetBits(num) for num in nums]
        bitCounts.sort()
        n = len(nums)
        pairs = 0
        print(bitCounts)
        
        for ind, c in enumerate(bitCounts):
            st = bisect_left(bitCounts, k - c)
            pairs += n - st
            
        return pairs