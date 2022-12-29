class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # bool "up" to keep track of direction
        up = True
        m = len(mat)
        n = len(mat[0])
        row = col = 0
        output = []
        
        for _ in range(m*n):
            
            output.append(mat[row][col])
            
            if up:
                if row - 1 < 0:
                    if col + 1 >= n:
                        row += 1
                    else:
                        col += 1
                    up = False
                else:
                    if col + 1 >= n:
                        row += 1
                        up = False
                    else:
                        row -= 1
                        col += 1
            else:
                if col - 1 < 0:
                    if row + 1 >= m:
                        col += 1
                    else:
                        row += 1
                    up = True
                else:
                    if row + 1 >= m:
                        col += 1
                        up = True
                    else:
                        row += 1
                        col -= 1
                        
        return output
                                