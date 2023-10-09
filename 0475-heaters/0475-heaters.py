class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        lh = len(heaters)
        
        dist = 0
        
        for house in houses:
            pos = bisect_left(heaters, house)
            best = min(abs(house - heaters[pos-1]), abs(heaters[min(pos, lh-1)] - house))
            dist = max(dist, best)
            
        return dist