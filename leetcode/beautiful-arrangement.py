class Solution:
    def countArrangement(self, n: int) -> int:
        arrangments = 0
        occ = 0
        
        def backtrack(num):
            nonlocal arrangments, occ
            if num > n:
                arrangments += 1
                return
            
            for numm in range(1, n+1):
                if not occ & 1 << numm and (not num % numm or not numm % num):
                    occ ^= 1 << numm
                    backtrack(num + 1)
                    occ ^= 1 << numm
                    
        backtrack(1)
        
        return arrangments
        