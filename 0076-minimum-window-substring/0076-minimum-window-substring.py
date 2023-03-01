class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = Counter(t)
        current = {lett:0 for lett in t}
        ans = [-float('inf'), float('inf')]
        
        for r in range(len(s)):
            lett = s[r]
            if lett in current:
                current[lett] += 1
            while all(current[letter] >= count[letter] for letter in current):
                leftLett = s[l]
                if leftLett in current:
                    current[leftLett] -= 1
                ans = min([ans, [l, r]], key=lambda x:x[1]-x[0])
                l += 1
                    
        if ans[0] == -float('inf'):
            return ""
        
        return s[ans[0]:ans[1]+1]