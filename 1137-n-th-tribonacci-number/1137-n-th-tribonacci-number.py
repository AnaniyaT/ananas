class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        
        if n < 3:
            return trib[n]
        
        for _ in range(n-2):
            trib.append(trib[-1] + trib[-2] + trib[-3])
            
        return trib[-1]