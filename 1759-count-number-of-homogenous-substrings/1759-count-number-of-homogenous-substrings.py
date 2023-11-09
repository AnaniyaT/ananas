class Solution:
    def countHomogenous(self, s: str) -> int:
        streak = 1
        cnt = 1
        
        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:
                streak += 1
            else:
                streak = 1
                
            cnt += streak
            
        return cnt % (10 ** 9 + 7)