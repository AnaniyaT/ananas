class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xoCount = defaultdict(int)
        for row in board:
            for col in row:
                xoCount[col] += 1
        if xoCount["X"] - xoCount["O"] > 1 or xoCount["O"] > xoCount["X"]:
            return False
        
        xWin = False
        oWin = False
        
        for row in board:
            sett = set(row)
            if len(sett) == 1:
                if "O" in sett:
                    oWin = True
                elif "X" in sett:
                    xWin = True
                    
        for col in range(3):
            sett = set()
            for row in range(3):
                sett.add(board[row][col])
            if len(sett) == 1:
                if "O" in sett:
                    oWin = True
                elif "X" in sett:
                    xWin = True
                    
        sett = set()
        for row in range(3):
            sett.add(board[row][row])
        if len(sett) == 1:
                if "O" in sett:
                    oWin = True
                elif "X" in sett:
                    xWin = True
                    
        sett = set()
        for row in range(3):
            sett.add(board[row][2 - row])
        if len(sett) == 1:
                if "O" in sett:
                    oWin = True
                elif "X" in sett:
                    xWin = True
                    
        if xWin and oWin:
            return False
        if xWin and xoCount["O"] == xoCount["X"]:
            return False
        if oWin and xoCount["O"] != xoCount["X"]:
            return False
        return True
        
        
        
    
                