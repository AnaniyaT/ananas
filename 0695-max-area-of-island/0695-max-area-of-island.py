class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def isValid(r, c):
            nonlocal m, n
            
            return 0 <= r < m and 0 <= c < n and grid[r][c]
        
        def dfs(r, c):
            size = 1
            for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + rOff, c + cOff
                
                if isValid(newR, newC) and (newR, newC) not in visited:
                    visited.add((newR, newC))
                    size += dfs(newR, newC)
                    
            return size
        
        maxSize = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c]:
                    visited.add((r, c))
                    maxSize = max(maxSize, dfs(r, c))
                    
        return maxSize
        