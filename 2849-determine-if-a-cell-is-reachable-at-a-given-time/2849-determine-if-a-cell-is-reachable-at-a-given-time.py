class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(sx - fx), abs (sy - fy))
        
        if not dist:
            return t != 1
        
        return t >= dist