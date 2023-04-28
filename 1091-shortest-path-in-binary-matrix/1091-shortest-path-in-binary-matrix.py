class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def isValid(r, c):
            inBound = 0 <= r < n and 0 <= c < n
            notVisited = (r, c) not in visited
            
            return inBound and notVisited and not grid[r][c]
        
        visited = set()
        queue = deque()
        if isValid(0, 0):
            queue.append((0, 0))
            visited.add((0, 0))
            
        lvl = 1
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r, c = queue.pop()
                if r == c == n-1:
                    return lvl

                for rOff in [-1, 0, 1]:
                    for cOff in [-1, 0, 1]:
                        newR, newC = r + rOff, c + cOff
                        if isValid(newR, newC):
                            visited.add((newR, newC))
                            queue.appendleft((newR, newC))
                        
            lvl += 1
            
        return -1
        