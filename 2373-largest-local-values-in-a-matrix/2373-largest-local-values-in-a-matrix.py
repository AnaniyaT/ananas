class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for startR in range(len(grid)-2):
            largestRow = []
            for startC in range(len(grid)-2):
                maxx = 0
                for row in range(3):
                    for col in range(3):
                        num = grid[startR+row][startC+col]
                        maxx = max(maxx, num)
                largestRow.append(maxx)

            result.append(largestRow)
            
        return result