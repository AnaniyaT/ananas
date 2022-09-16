class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = []
        longest = l = r = 0
        while r < len(s):
            if s[r] not in sett:
                sett.append(s[r])
                longest = max(longest, len(sett))
                r += 1
            else:
                sett.remove(s[l])
                l += 1
        return longest