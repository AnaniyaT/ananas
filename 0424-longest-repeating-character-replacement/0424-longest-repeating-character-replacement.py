class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        
        for target in range(ord('A'), ord('Z') + 1):
            
            l = 0
            replaced = 0
            for r in range(len(s)):
                if ord(s[r]) != target:
                    replaced += 1
                while replaced > k:
                    if ord(s[l]) != target:
                        replaced -= 1
                    l += 1
                        
                maxLen = max(maxLen, r-l+1)
                
        return maxLen