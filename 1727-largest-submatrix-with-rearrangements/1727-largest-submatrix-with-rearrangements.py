class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        for col in range(m):
            for row in range(1, n):
                if matrix[row][col]:
                    matrix[row][col] += matrix[row-1][col]
        
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for idx, h in enumerate(row):
                ans = max(ans, h * (idx + 1))
        
        return ans