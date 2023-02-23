class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] += 1
        subarrays = 0
        odds = 0
        
        for num in nums:
            if num%2:
                odds += 1
            
            subarrays += count[odds-k]
            count[odds] += 1
            
        return subarrays
            