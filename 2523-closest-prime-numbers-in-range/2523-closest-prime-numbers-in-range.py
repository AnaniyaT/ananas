class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [0 for _ in range(right+1)]
        
        for d in range(2, int((right)**0.5) + 1):
            if d == 2 or d % 2:
                for m in range(2, int(right/d) + 1):
                    sieve[d * m] = 1
                    
        inf = float('inf')
        ans = [-inf, inf]
        prev = -inf
        
        for num in range(max(2, left), right+1):
            if not sieve[num]:
                if num - prev < ans[1] - ans[0]:
                    ans[0], ans[1] = prev, num
                prev = num
            
        if ans[0] == -inf:
            return [-1, -1]
        
        return ans