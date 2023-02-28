class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        mySet = set(3**i for i in range(26))
        
        if n in mySet:
            return True
        else:
            return False