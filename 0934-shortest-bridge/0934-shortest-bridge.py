class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = set()
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        def dfs(r, c):
            visited.add((r, c))
            grid[r][c] = 0
            queue.append((r, c))
            
            for a, b in directions:
                nr, nc = r + a, c + b
                if isValid(nr, nc) and (nr, nc) not in visited and grid[nr][nc]:
                    dfs(nr, nc)
        
        for r in range(n):
            if queue:
                break
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    break
                    
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                a, b = queue.pop()
                
                if grid[a][b]:
                    return step - 1
                
                for ro, co in directions:
                    nr, nc = a + ro, b + co
                    if isValid(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.appendleft((nr, nc))
                        
            step += 1