class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if rows*cols != r*c:
            return mat
        
        reshaped = [[0]*c for _ in range(r)]
        
        for ind in range(rows*cols):
            row = ind//cols
            col = ind%cols
            
            row1 = ind//c
            col1 = ind%c
            
            reshaped[row1][col1] = mat[row][col]
            
        return reshaped