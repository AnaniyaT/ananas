class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1 / x
        
        half = self.myPow(x, n // 2)
        ans = half * half
        
        if n % 2:
            ans *= x
            
        return ans
        
