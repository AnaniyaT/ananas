class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #not my idea
        prefix = list(accumulate(stones))
        
        @cache
        def bac(curSum, ind):
            if curSum + prefix[ind] < 0:
                return float('inf')
            
            if ind < 0:
                if curSum >= 0:
                    return curSum
                
                return float('inf')
            
            neg = bac(curSum - stones[ind], ind-1)
            pos = bac(curSum + stones[ind], ind-1)
            
            return min(neg, pos)
        
        return bac(0, len(stones) - 1)
        
        