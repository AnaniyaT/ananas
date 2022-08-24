class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        temp = n
        while temp != 1:
            if temp%3 != 0:
                return False
            temp = temp/3
        return True
            
            