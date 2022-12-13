class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        for r in range(n-2, -1, -1):
            for c in range(n):
                if c == 0:
                    matrix[r][c] += min(matrix[r+1][0], matrix[r+1][1])
                elif c == n-1:
                    matrix[r][c] += min(matrix[r+1][c], matrix[r+1][c-1])
                else:
                    matrix[r][c] += min(matrix[r+1][c], matrix[r+1][c-1], matrix[r+1][c+1])
        return min(matrix[0])
            
            