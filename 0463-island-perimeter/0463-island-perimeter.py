class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def isInBound(y, x):
            return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
        
        visited = set()
        perimeter = 0
        
        def dfs(y, x):
            nonlocal perimeter
            visited.add((y, x))
            
            for yOff, xOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newY, newX = y + yOff, x + xOff
                
                if isInBound(newY, newX) and (newY, newX) not in visited and grid[newY][newX]:
                    dfs(newY, newX)
                elif (newY, newX) not in visited:
                    perimeter += 1
                    
        for ind in range(len(grid) * len(grid[0])):
            r = ind // len(grid[0])
            c = ind % len(grid[0])
            
            if grid[r][c]:
                dfs(r, c)
                break
                
        return perimeter