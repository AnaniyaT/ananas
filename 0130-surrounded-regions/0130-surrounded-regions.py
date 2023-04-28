class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def isValid(r, c):
            inBound = 0 <= r < m and 0 <= c < n
            
            return inBound and board[r][c] == "O"
        
        def dfs(r, c):
            board[r][c] = "b"
            
            for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + rOff, c + cOff
                
                if isValid(newR, newC):
                    dfs(newR, newC)
                    
        for r in [0, m-1]:
            for c in range(n):
                if isValid(r, c):
                    dfs(r, c)
                    
        for c in [0, n-1]:
            for r in range(m):
                if isValid(r, c):
                    dfs(r, c)
                    
        for r in range(m):
            for c in range(n):
                if board[r][c] == "b":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
                    