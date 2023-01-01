class Solution:
    def numSub(self, s: str) -> int:
        #Dani's Code
        
        l = 0
        subarrays = 0
        for ind, char in enumerate(s):
            if s[ind] == "0":
                l = ind + 1
            subarrays += ind - l + 1

        return subarrays % (10**9 + 7)