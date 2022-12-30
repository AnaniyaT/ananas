class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        
        # List to store the num of ones of each row and columns
        rowOnes = [0 for _ in range(rows)]
        columnOnes = [0 for _ in range(columns)]
        
        diff = [[0 for _ in range(columns)] for _ in range(rows)]
        
        # Building rowOnes and columnOnes
        for row in range(rows):
            for col in range(columns):
                gridVal = grid[row][col]
                rowOnes[row] += gridVal
                columnOnes[col] += gridVal
        
        # Building the final diff matrix
        for row in range(rows):
            rowZeros = columns - rowOnes[row]
            for col in range(columns):
                columnZeros = rows - columnOnes[col]
                diff[row][col] = rowOnes[row] + columnOnes[col] - rowZeros - columnZeros
        
        return diff
        