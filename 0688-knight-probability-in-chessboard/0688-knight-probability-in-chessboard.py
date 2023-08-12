class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def isInside(r, c):
            return 0 <= r < n and 0 <= c < n
        
        directions = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        cache = {}
        
        def rec(r, c, k):
            if (r, c, k) in cache:
                return cache[(r, c, k)]
            
            inside = isInside(r, c)
            if not k:
                return int(isInside(r, c))
            
            if not inside:
                return 0
            
            probs = 0
            
            for rOff, cOff in directions:
                newR, newC = r + rOff, c + cOff
                probs += rec(newR, newC, k - 1) / 8
                
            cache[(r, c, k)] = probs
            
            return probs
        
        return rec(row, column, k)
            