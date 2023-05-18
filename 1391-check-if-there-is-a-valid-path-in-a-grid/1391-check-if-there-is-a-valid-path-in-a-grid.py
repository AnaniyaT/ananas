class UnionFind:
    def __init__(self, n, edges=[]) -> None:
        self.rep = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
        for fro, to in edges:
            self.union(fro, to)
    
    def findRep(self, x):
        cur = x
        while cur != self.rep[cur]:
            cur = self.rep[cur]
            
        while x != cur:
            prev = self.rep[x]
            self.rep[x] = cur
            x = prev
            
        return cur
        
    def union(self, x, y):
        repX, repY = self.findRep(x), self.findRep(y)
        
        if repX == repY:
            return
        
        if self.rank[repX] >= self.rank[repY]:
            repX, repY = repY, repX
            
        self.rep[repX] = repY
        self.rank[repY] += self.rank[repX]
            
    def isConnected(self, x, y):
        return self.findRep(x) == self.findRep(y)
    
    
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        paths = UnionFind(m * n)
        pathsReal = UnionFind(m * n)
        
        con = [
                [(0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (1, 0)],
                [(0, 1), (1, 0)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)]
            ]
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < m
        
        for ind in range(m * n):
            r = ind // m
            c = ind % m
            
            cell = grid[r][c]
            
            (r1off, c1off), (r2off, c2off) = con[cell - 1]
            
            newr1, newc1, newr2, newc2 = r + r1off, c + c1off, r + r2off, c + c2off
            if isValid(newr1, newc1):
                f = newr1 * m + newc1
                if paths.isConnected(ind, f):
                    pathsReal.union(ind, f)
                else:
                    paths.union(ind, f)
                
            if isValid(newr2, newc2):
                s = newr2 * m + newc2
                if paths.isConnected(ind, s):
                    pathsReal.union(ind, s)
                else:
                    paths.union(ind, s)
       
        return pathsReal.isConnected(0, n * m - 1)
            
            
            
            