class Solution(object):
    def isPalindrome(self, s):
        word = ""
        for char in s:
            if char.isalnum():
                word += char.lower()
                
        r, l = len(word)-1, 0
        while l < r:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
