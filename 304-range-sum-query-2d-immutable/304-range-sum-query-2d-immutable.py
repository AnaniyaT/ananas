class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.summ = [[0]*(col+1) for i in range(row+1)]
        for r,i in enumerate(matrix):
            rowsum = 0
            for c,j in enumerate(i):
                rowsum += j
                self.summ[r+1][c+1] = self.summ[r][c+1] + rowsum
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summ[row2+1][col2+1]-self.summ[row1][col2+1]-self.summ[row2+1][col1]+self.summ[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)