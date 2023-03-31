class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = [1 for _ in range(n)]
        
        primes[0] = primes[1] = 0
        root = int(n ** 0.5)
        
        for ind in range(root + 1):
            if primes[ind]:
                for mul in range(ind * ind, n , ind):
                    primes[mul] = 0
       
                    
        return sum(primes)
                    