class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for colInd in range(cols):
                        if colInd != col and matrix[row][colInd] != 0:
                            matrix[row][colInd] = "b"
                    for rowInd in range(rows):
                        if rowInd != row and matrix[rowInd][col] != 0:
                            matrix[rowInd][col] = "b"
                            
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "b":
                    matrix[row][col] = 0
        
                        
                    