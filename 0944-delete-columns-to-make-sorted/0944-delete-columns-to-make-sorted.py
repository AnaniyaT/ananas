class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedCols = 0
        rows = len(strs)
        for col in range(len(strs[0])):
            maxx = 0
            for row in range(rows):
                ordd = ord(strs[row][col])
                if ordd < maxx:
                    deletedCols += 1
                    break
                maxx = ordd
                    
        return deletedCols