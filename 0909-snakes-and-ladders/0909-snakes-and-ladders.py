class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        sq = n * n
        
        def getRC(no):
            row = (no - 1) // n
            
            r = n - row - 1
            off = no - (row * n) - 1
            
            if not row % 2:
                c = off
                
            else:
                c = n - off - 1
                
            return r, c
        
        
        visited = set([1])
        queue = deque([1])
        level = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                cur = queue.pop()
                if cur == sq:
                    return level
                
                for add in range(1, 7):
                    new = cur + add
                    newR, newC = getRC(new)
                    
                    if new <= sq and board[newR][newC] != -1 and board[newR][newC] not in visited:
                        visited.add(board[newR][newC])
                        queue.appendleft(board[newR][newC])
                        
                    elif new not in visited and new <= sq and board[newR][newC] == -1:
                        visited.add(new)
                        queue.appendleft(new)
                        
            level += 1
            
            
        return -1
                
                
                