class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)
        
        l = 0
        fulfilled = 0
        cur = {}
        for r in range(len(s2)):
            cur[s2[r]] = cur.get(s2[r], 0) + 1
            if cur[s2[r]] == counts1.get(s2[r], 0):
                fulfilled += 1
            
            if r - l >= len(s1):
                if cur[s2[l]] == counts1.get(s2[l], 0):
                    fulfilled -= 1
                    
                cur[s2[l]] -= 1
                l += 1
                
            if fulfilled == len(counts1):
                return True
            
        return False
