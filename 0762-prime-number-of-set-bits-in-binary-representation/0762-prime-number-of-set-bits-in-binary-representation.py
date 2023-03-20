class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        sets = 0
        
        for num in range(left, right + 1):
            ones = 0
            while num:
                ones += num % 2
                num //= 2
                
            if ones in primes:
                sets += 1
                
        return sets