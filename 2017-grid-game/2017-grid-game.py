class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        
        for row in grid:
            row.append(0)
            for ind in range(1, length):
                row[ind] += row[ind-1]
            
        minR2Score = float('inf')
        
        for ind in range(length):
            row1 = grid[0][length-1] - grid[0][ind]
            row2 = grid[1][ind-1]
            r2Score = max(row1, row2)
            minR2Score = min(minR2Score, r2Score)
        
        return minR2Score