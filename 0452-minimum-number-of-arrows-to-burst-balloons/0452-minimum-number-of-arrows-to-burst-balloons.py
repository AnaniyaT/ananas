class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = len(points)
        
        points.sort()
        ext = points[0][1]
        
        for s, e in points[1:]:
            if s <= ext:
                arrows -= 1
                ext = min(ext, e)
            else:
                ext = e
            
        return arrows