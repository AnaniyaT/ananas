class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowSet = set()
        colSet = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowSet.add(row)
                    colSet.add(col)
                    
        for row in rowSet:
            for col in range(cols):
                matrix[row][col] = 0
                
        for col in colSet:
            for row in range(rows):
                matrix[row][col] = 0
                
        
                        
                    