class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        y, x = click
        
        
        def isValid(y, x):
            return 0 <= y < n and 0 <= x < m
        
        def adjacentMines(y, x):
            count = 0
            for yOff, xOff in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                newY, newX = y + yOff, x + xOff
                
                if isValid(newY, newX) and board[newY][newX] == "M":
                    count += 1
                    
            return count
        
        if board[y][x] == "M":
            board[y][x] =  "X"
            return board
        
        if board[y][x] == "E":
                adjacent_mines = adjacentMines(y, x)
                if adjacent_mines:
                    board[y][x] = str(adjacent_mines)
                    
                    return board
                else:
                    board[y][x] = "B"
        
        
        queue = deque([click])
        
        while queue:
            y, x = queue.pop()
                    
            for yOff, xOff in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                newY, newX = y + yOff, x + xOff

                if isValid(newY, newX) and board[newY][newX] == "E":
                    adjacent_mines = adjacentMines(newY, newX)
                    if adjacent_mines:
                        board[newY][newX] = str(adjacent_mines)
                    else:
                        board[newY][newX] = "B"
                        queue.appendleft((newY, newX))
                    
        return board
