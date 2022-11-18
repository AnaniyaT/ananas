class Solution(object):
    def reverse(self, x):
        reversedd = int(str(abs(x))[::-1])
        if x < 0: reversedd *= -1
        if abs(reversedd) > 2**31-1:
            return 0
        return reversedd
        