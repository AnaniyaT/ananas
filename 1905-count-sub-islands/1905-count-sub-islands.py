class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid2[0])
        
        def isValid(r, c):
            inBound = 0 <= r < m and 0 <= c < n
            notVisited = (r, c) not in visited
            
            return inBound and notVisited and grid2[r][c]
        
        visited = set()
        
        def dfs(r, c):
            ret = True
            visited.add((r, c))
            
            for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + rOff, c + cOff
                
                if isValid(newR, newC):
                    if not dfs(newR, newC) or not grid1[newR][newC]:
                        ret = False
                    
            return ret
        
        
        subIslands = 0
        for r in range(m):
            for c in range(n):
                if isValid(r, c) and dfs(r, c) and grid1[r][c]:
                    subIslands += 1
                    
        return subIslands