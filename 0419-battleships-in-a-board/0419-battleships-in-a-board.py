class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        counter = 0
        for rowNo, row in enumerate(board):
            for col, cell in enumerate(row):
                leftCell = "."
                topCell = "."
                if rowNo > 0:
                    topCell = board[rowNo-1][col]
                if col > 0:
                    leftCell = board[rowNo][col-1]
                if cell == "X":
                    if leftCell != ".":
                        board[rowNo][col] = leftCell
                    elif topCell != ".":
                        board[rowNo][col] = topCell
                    else:
                        counter += 1
                        board[rowNo][col] = counter
        return counter