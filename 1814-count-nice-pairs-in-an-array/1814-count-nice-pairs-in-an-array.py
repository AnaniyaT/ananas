class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        count = 0
        
        for num in nums:
            revDiff = num - int(str(num)[::-1])
            count += counts[revDiff]
            counts[revDiff] += 1
            
        mod = 10 ** 9 + 7
        
        return count % mod