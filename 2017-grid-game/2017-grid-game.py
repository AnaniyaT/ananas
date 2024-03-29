class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        
        for row in grid:
            # adding a buffer at the end
            row.append(0)
            
            # calculating prefix sum
            for ind in range(1, length):
                row[ind] += row[ind-1]
            
        minR2Score = float('inf')
        
        
        for ind in range(length):
            # possible paths left for robot2 (either row1 or row2)
            row1 = grid[0][length-1] - grid[0][ind]
            row2 = grid[1][ind-1]
            
            # robot 2 will choose the maximum of the two paths
            r2Score = max(row1, row2)
            
            # robot 1 will try to minimize the score of robot 2
            minR2Score = min(minR2Score, r2Score)
        
        return minR2Score