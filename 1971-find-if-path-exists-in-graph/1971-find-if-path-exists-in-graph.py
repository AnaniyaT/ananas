class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def findRep(x):
            cur = x
            while cur != rep[cur]:
                cur = rep[cur]
                
            while x != cur:
                prev = rep[x]
                rep[x] = cur
                x = prev
                
            return cur
                
        def union(x, y):
            repX, repY = findRep(x), findRep(y)
            
            if rank[repX] < rank[repY]:
                rep[repX] = repY
                rank[repY] += rank[repX]
            else:
                rep[repX] = repX
                rep[repY] = repX
                rank[repX] += rank[repY]
                
        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        for fro, to in edges:
            union(fro, to)
            
        # print(rep)
        # print(rank)
        return isConnected(source, destination)
        
                
            