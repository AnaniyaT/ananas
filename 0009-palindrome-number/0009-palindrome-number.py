class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        return number == number[::-1]