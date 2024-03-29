class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = matrix
        self.sumMatrix.append([0]*len(matrix[0]))
        
        for row in self.sumMatrix:
            row.append(0)
            
        for row in range(len(self.sumMatrix)-1):
            for col in range(len(self.sumMatrix[0])-1):
                left = self.sumMatrix[row][col-1]
                top = self.sumMatrix[row-1][col]
                topLeft = self.sumMatrix[row-1][col-1]
                
                self.sumMatrix[row][col] += left + top - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.sumMatrix[row2][col1-1]
        top = self.sumMatrix[row1-1][col2]
        topLeft = self.sumMatrix[row1-1][col1-1]
        bottomG = self.sumMatrix[row2][col2]
        
        return bottomG - left - top + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)