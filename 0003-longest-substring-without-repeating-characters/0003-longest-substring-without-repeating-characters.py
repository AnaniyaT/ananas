class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        window = set()
        
        for r, lett in enumerate(s):
            window.add(lett)
            if r-l+1 != len(window):
                while s[l] != lett:
                    window.remove(s[l])
                    
                    l += 1    
                l += 1
            
            longest = max(longest, r-l+1)

        return longest