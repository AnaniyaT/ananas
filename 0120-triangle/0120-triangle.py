class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle)-2, -1, -1):
            row = triangle[r]
            for c in range(len(row)):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
                
        return triangle[0][0]