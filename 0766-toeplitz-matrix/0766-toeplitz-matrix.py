class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals = defaultdict(set)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = matrix[row][col]
                diagonals[row-col].add(num)
                if len(diagonals[row-col]) > 1:
                    return False
                
        return True