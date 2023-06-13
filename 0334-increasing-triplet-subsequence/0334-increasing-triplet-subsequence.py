class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        inf = float('inf')
        cur = inf
        
        minn = inf
        for num in nums:
            if num > cur:
                return True
            
            if num > minn:
                cur = num
                
            minn = min(minn, num)
            
        return False