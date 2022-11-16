# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, a = 1) -> int:
        bro = (a+n)//2
        if guess(bro) == 0:
            return bro
        elif guess(bro) == -1:
            return self.guessNumber(bro - 1, a)
        else:
            return self.guessNumber(n, bro + 1)