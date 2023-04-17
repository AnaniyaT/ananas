class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        for ind in range(1, len(binary)):
            if binary[ind] == binary[ind-1]:
                return False
            
        return True