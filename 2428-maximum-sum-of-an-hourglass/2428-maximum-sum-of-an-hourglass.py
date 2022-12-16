class Solution(object):
    def maxSum(self, grid):
        for row in range(len(grid)):
            for col in range(1,len(grid[0])):
                grid[row][col] += grid[row][col-1]
        maxSumm = 0
        print (grid)
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                summ = grid[row][col+2] + grid[row+1][col+1] - grid[row+1][col] + grid[row+2][col+2]
                if col > 0:
                    summ -= grid[row][col-1] + grid[row+2][col-1]
                maxSumm = max(maxSumm, summ)
        return maxSumm
        