class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def rec(tar):
            if tar in cache:
                return cache[tar]
            
            if not tar:
                return 1
            if tar < 0:
                return 0
            
            ways = 0
            for num in nums:
                ways += rec(tar-num)
                
            cache[tar] = ways
            
            return ways
        
        return rec(target)