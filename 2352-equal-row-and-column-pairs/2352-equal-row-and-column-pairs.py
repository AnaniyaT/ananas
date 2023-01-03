class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = defaultdict(int)
        for row in grid:
            rowDict[tuple(row)] += 1
        count = 0
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            
            count += rowDict[tuple(column)]
            
        return count