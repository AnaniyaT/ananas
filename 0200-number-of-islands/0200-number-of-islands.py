class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isInBound(y, x):
            return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
        
        visited = set()
        islands = 0
        
        def dfs(y, x):
            visited.add((y, x))
            
            for yOff, xOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newY, newX = y + yOff, x + xOff
                if isInBound(newY, newX) and grid[newY][newX] == "1" and (newY, newX) not in visited:
                    dfs(newY, newX)
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
                    
        return islands