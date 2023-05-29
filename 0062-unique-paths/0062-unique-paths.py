class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
        grid[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                ways = grid[row-1][col] + grid[row][col-1]
                grid[row][col] += ways
                
        return grid[m-1][n-1]