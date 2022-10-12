class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vSet = set("aeiou")
        l = r = maxx = count = 0
        while r < k:
            if s[r] in vSet:
                count += 1
            r += 1
        maxx = count
        while r < len(s):
            if s[l] in vSet:
                count -= 1
            if s[r] in vSet:
                count += 1
            l += 1
            r += 1
            maxx = max(maxx, count)
            
        return maxx