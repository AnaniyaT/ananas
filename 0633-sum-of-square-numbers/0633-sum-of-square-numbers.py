class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxx = int(c**(0.5))
        r = maxx
        for l in range(maxx+1):
            if l > r:
                return False
            
            while l**2 + r**2 > c:
                r -= 1
            
            if l**2 + r**2 == c:
                return True