class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = odd = n // 2
        
        if n % 2:
            even += 1
        
        mod = 10 ** 9 + 7
        
        return (pow(4, odd, mod) * pow(5, even, mod)) % mod
      
        