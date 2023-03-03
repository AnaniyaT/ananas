# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        mid = lo + (hi-lo)//2
        
        while lo < hi:
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
                
            mid = lo + (hi-lo)//2
                
        return mid