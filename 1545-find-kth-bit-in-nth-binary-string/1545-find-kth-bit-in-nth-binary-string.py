class Solution:
    def findNthString(self, n):
        if n == 1:
            return ["0"]
        
        previous = self.findNthString(n-1)
        inverted = ["0" if int(previous[ind]) else "1" for ind in range(len(previous))]
        previous.append("1")
        current = previous + inverted[::-1]
        
        return current
        
    def findKthBit(self, n: int, k: int) -> str:
        nthString = self.findNthString(n)
        
        return nthString[k-1]