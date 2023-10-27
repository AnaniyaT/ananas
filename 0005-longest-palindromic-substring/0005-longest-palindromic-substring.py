class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = (0,0)
        n = len(s)
        for start in range(n):
            l = r = start
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            if best[1] - best[0] < r - l:
                best = (l, r)
            
            l, r = start, start + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            if best[1] - best[0] < r - l:
                best = (l, r)
            
        return s[best[0]+1:best[1]]