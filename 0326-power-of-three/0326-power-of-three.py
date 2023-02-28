class Solution:
    def __init__(self):
        self.mySet = {1, 3, 9, 2187, 3486784401, 27, 6561, 59049, 43046721, 129140163, 387420489, 81, 1594323, 729, 1162261467, 19683, 14348907, 531441, 243, 4782969, 177147}

    def isPowerOfThree(self, n: int) -> bool:
        if n in self.mySet:
            return True
        else:
            return False
