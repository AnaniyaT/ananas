class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = Counter(t)
        current = {lett:0 for lett in t}
        ans = ""
        
        for r in range(len(s)):
            lett = s[r]
            if lett in current:
                current[lett] += 1
            while all([current[letter] >= count[letter] for letter in current]):
                leftLett = s[l]
                if leftLett in current:
                    current[leftLett] -= 1
                if r-l < len(ans) or not ans:
                    ans = s[l:r+1]
                l += 1
                    
        return ans