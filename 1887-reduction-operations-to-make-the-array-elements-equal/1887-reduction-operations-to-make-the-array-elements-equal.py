class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        count = 0
        
        pref = 0
        for num in sorted(counts, reverse=True)[:-1]:
            count += counts[num] + pref
            pref += counts[num]
            
        return count
        
        