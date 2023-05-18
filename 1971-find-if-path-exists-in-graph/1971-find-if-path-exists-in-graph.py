
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
        
        if repY == repX:
            return
        
        if self.rank[repX] >= self.rank[repY]:
            repX, repY = repY, repX
            
        self.rep[repX] = repY
        self.rank[repY] += self.rank[repX]
            
    def isConnected(self, x, y):
        return self.findRep(x) == self.findRep(y)
    
    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        paths = UnionFind(n, edges)
        return paths.isConnected(source, destination)
        
                
            