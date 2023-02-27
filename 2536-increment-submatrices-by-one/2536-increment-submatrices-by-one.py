class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*(n+1) for _ in range(n+1)]
        
        for row1, col1, row2, col2 in queries:
            matrix[row1][col1] += 1
            matrix[row1][col2+1] -= 1
            matrix[row2+1][col1] -= 1
            matrix[row2+1][col2+1] += 1
            
        for row in range(n):
            runSum = 0
            for col in range(n):
                runSum += matrix[row][col]
                matrix[row][col] = runSum
                
        for col in range(n):
            runSum = 0
            for row in range(n):
                runSum += matrix[row][col]
                matrix[row][col] = runSum
                
        matrix.pop()
        for row in matrix:
            row.pop()
            
        return matrix
        