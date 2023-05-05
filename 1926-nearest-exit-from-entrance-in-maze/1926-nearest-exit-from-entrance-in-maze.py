class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        
        def isValid(r, c):
            inBound = 0 <= r < n and 0 <= c < m
            notVisited = (r, c) not in visited
            return inBound and maze[r][c] == "." and notVisited
        
        def isGoal(r, c):
            notEntrance = [r, c] != entrance
            isBorder = r in [0, n-1] or c in [0, m-1]
            
            return notEntrance and isBorder
        
        queue = deque([tuple(entrance)])
        visited = set([tuple(entrance)])
        
        level = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r, c = queue.pop()
                
                if isGoal(r, c):
                    return level
                
                for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR, newC = r + rOff, c + cOff
                    
                    if isValid(newR, newC):
                        visited.add((newR, newC))
                        queue.appendleft((newR, newC))
                        
            level += 1
            
        
        return -1
                
            