class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal = [[1,2,3], [4,5,0]]
        
        def toTup(arr):
            return (tuple(arr[0]), tuple(arr[1]))
        
        def toLst(tup):
            return [list(tup[0]), list(tup[1])]
        
        def isValid(x, y):
            return 0 <= x < 2 and 0 <= y < 3
        
        def neighbours(state):
            states = []
            for i in range(2):
                for j in range(3):
                    if state[i][j] == 0:
                        r, c = i, j
                        
            for a, b in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                n, m = r + a, c + b
                if isValid(n, m):
                    newState = toLst(state)
                    newState[r][c], newState[n][m] = newState[n][m], newState[r][c]
                    
                    yield newState
                    
        queue = deque([board])
        visited = set(toTup(board))
        step = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                cur = queue.pop()
                
                if cur == goal:
                    return step
                
                for neigh in neighbours(cur):
                    tup = toTup(neigh)
                    if tup not in visited:
                        visited.add(tup)
                        queue.appendleft(neigh)
                        
            step += 1
            
        return -1
                        
                        
        