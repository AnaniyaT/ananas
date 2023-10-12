class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        kmp = [0] * n
        
        l, i = 0, 1
        
        while i < n:
            if s[l] == s[i]:
                l += 1
                kmp[i] = l
                i += 1
            else:
                if l == 0:
                    i += 1
                else:
                    l = kmp[l-1]
        
        return s[:kmp[-1]]