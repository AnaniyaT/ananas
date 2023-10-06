class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        @cache
        def find(clip,  cur):
            if cur == n:
                return 0
            
            if cur > n:
                return float('inf')
            
            copy = float('inf')
            paste = float('inf')
            
            if clip != cur:
                copy = find(cur, cur)
                
            paste = find(clip, cur + clip)
            
            return min(copy, paste) + 1
        
        return find(1, 1) + 1
