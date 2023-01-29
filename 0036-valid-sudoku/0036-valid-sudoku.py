class Solution:
    def isValidBox(self, board, startR, startC):
        nums = set()
        for row in range(startR, startR+3):
            for col in range(startC, startC+3):
                if board[row][col] in nums:
                    return False
                if board[row][col] != ".":
                    nums.add(board[row][col])
                    
        return True
                    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        colNums = defaultdict(set)
        
        # checking for the rows and columns
        for row in range(rows):
            nums = set()
            for col in range(cols):
                if board[row][col] in nums:
                    return False
                if board[row][col] in colNums[col]:
                    return False
                
                if board[row][col] != ".":
                    nums.add(board[row][col])
                    colNums[col].add(board[row][col])
        
        # checking for the 3x3 boxes
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not self.isValidBox(board, row, col):
                    return False
                
        return True
                
        
        