class Solution:
    def minSteps(self, n: int) -> int:
        def primeFactors(n):
            primeFactors = []
            for d in range(2, int(n**0.5) + 1):
                while not n % d:
                    n = n//d
                    primeFactors.append(d)
                    
            if n > 1:
                primeFactors.append(n)
                
            return primeFactors
        
        return sum(primeFactors(n))