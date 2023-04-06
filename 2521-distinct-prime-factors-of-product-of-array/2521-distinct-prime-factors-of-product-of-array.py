class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactors = set()
        
        for num in nums:
            for n in range(2, int(num**0.5)+1):
                while num and not num % n:
                    primeFactors.add(n)
                    num //= n
                
            if num != 1:
                primeFactors.add(num)
        
        return len(primeFactors)
                    
            
            