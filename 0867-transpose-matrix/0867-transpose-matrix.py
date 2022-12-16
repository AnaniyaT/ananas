class Solution(object):
    def transpose(self, matrix):
        transpose = [[0 for _ in range(len(matrix))] for _ in range (len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transpose[col][row] = matrix[row][col]
        return transpose