class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        start, end = 0, x//2
        
        while start <= end:
            mid = start + (end - start)//2
            square = mid * mid
            
            if square < x:
                start = mid + 1
            elif square > x:
                end = mid - 1
            else:
                return mid
            
        return end