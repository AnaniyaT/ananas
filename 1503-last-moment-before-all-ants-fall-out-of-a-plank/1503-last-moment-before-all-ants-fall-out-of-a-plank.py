class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxx = 0
        
        if left:
            maxLefts = max(left)
            maxx = max(maxx, maxLefts)
        if right:
            maxRights = n - min(right)
            maxx = max(maxx, maxRights)
            
        return maxx