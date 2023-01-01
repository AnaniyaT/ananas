class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        subarrays = 0
        for ind, char in enumerate(s):
            while l < ind and s[l] == "0":
                l += 1
            if char == "1":
                subarrays += ind - l + 1
            else:
                l = ind
        return subarrays % (10**9 + 7)