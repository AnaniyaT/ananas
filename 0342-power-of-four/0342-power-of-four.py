class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        myLog = log(n)/log(4)
        
        return int(myLog) == myLog