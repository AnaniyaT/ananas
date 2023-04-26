class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def isValid(r, c):
            isInbound = 0 <= r < m and 0 <= c < n
            notVisited = (r, c) not in visited
            
            return isInbound and notVisited and grid[r][c] == 1
        
        queue = deque()
        oranges = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.appendleft((r, c))
                elif grid[r][c]:
                    oranges += 1
                    
        minutes = 0
        
        while queue and oranges:
            size = len(queue)
            
            for _ in range(size):
                r, c = queue.pop()
                for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR, newC = r + rOff, c + cOff
                    
                    if isValid(newR, newC):
                        visited.add((newR, newC))
                        queue.appendleft((newR, newC))
                        oranges -= 1
                        
            minutes += 1
            
        if not oranges:
            return minutes
        else:
            return -1
                    
        