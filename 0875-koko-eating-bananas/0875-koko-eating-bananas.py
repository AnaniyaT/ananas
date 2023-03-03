class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(speed):
            hours = 0
            
            for pile in piles:
                if pile <= speed:
                    hours += 1
                else:
                    hours += ceil(pile/speed)
                    
            return hours
        
        
        start, end = 1, max(piles)
        
        while start <= end:
            mid = start + (end - start) // 2
            
            hours = hoursTaken(mid)
            
            if hours > h:
                start = mid + 1
            else:
                end = mid - 1
                
        return start