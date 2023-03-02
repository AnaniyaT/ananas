class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
    
        size = 2 ** ceil(log(k)/log(2))
        off = size - k
        inverse = size//2 - off
        
        
        return int(not(self.kthGrammar(n, inverse)))