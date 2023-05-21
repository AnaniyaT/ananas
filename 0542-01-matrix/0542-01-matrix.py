class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < m
        
        queue = deque()
        for r in range(n):
            for c in range(m):
                if not mat[r][c]:
                    queue.append((r, c))
    
        visited = set()
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.pop()
                
                mat[r][c] = step
                
                for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR, newC = r + rOff, c + cOff
                    if isValid(newR, newC) and mat[newR][newC] and (newR, newC) not in visited:
                        queue.appendleft((newR, newC))
                        visited.add((newR, newC))
            step += 1
            
        return mat
                        
                
        