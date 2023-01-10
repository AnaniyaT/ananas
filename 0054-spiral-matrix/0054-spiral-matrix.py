class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirn = "r"
        limits = [1, len(matrix[0])-1, len(matrix)-1, 0]
        row = 0
        col = 0
        answer = []
        for _ in range(len(matrix)*len(matrix[0])):
            answer.append(matrix[row][col])
            if dirn == "r":
                if col == limits[1]:
                    dirn = "d"
                    limits[1] -= 1
                    row += 1
                else:
                    col += 1
            elif dirn == "d":
                if row == limits[2]:
                    dirn = "l"
                    limits[2] -= 1
                    col -= 1
                else:
                    row += 1
            elif dirn == "l":
                if col == limits[3]:
                    dirn = "u"
                    limits[3] += 1
                    row -= 1
                else:
                    col -= 1
            else:
                if row == limits[0]:
                    dirn = "r"
                    limits[0] += 1
                    col += 1
                else:
                    row -= 1
        
        return answer
                
            