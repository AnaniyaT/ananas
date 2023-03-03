class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysTaken(cap):
            days = 1
            weight = 0
            
            for w in weights:
                weight += w
                if weight > cap:
                    days += 1
                    weight = w
                    
            return days
        
        start, end = max(weights), sum(weights)
        
        while start <= end:
            mid = start + (end - start)//2
            
            timeTaken = daysTaken(mid)
            
            if timeTaken <= days:
                end = mid - 1
                
            else:
                start = mid + 1
                
        return start