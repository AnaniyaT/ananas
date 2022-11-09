class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = p2 = 0
        while p1 < len(haystack):
            if haystack[p1] == needle[p2]:
                if p2 == len(needle)-1:
                    return p1-p2
                p2 += 1
            else:
                p1 -= p2
                p2 = 0
            p1 += 1
        return -1