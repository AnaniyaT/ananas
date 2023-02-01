class Solution:
    def checkSquare(self, grid, startR, startC):
        prev = 0
        prev1 = 0
        diag1 = 0
        diag2 = 0
        nums = set()
        for row in range(3):
            summ = 0
            summ1 = 0
            for col in range(3):
                summ += grid[startR+row][startC+col]
                summ1 += grid[startR+col][startC+row]
                if row == col:
                    diag1 += grid[startR+row][startC+col]
                if row + col == 2:
                    diag2 += grid[startR+row][startC+col]
                nums.add(grid[startR+row][startC+col])
                
            if (prev and summ != prev) or (prev1 and summ1 != prev1):
                return False
            prev = summ
            prev1 = summ1
            
        if (not (prev == prev1 == diag1 == diag2)) or nums != {1,2,3,4,5,6,7,8,9}:
            return False
        
        return True
        
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
        
        magicSquares = 0
        for startR in range(rows-2):
            for startC in range(cols-2):
                if self.checkSquare(grid, startR, startC):
                    magicSquares += 1
                    
        return magicSquares
        
        
        