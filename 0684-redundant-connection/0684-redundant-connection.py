class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redundant = []
        rep = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]
        
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
            nonlocal redundant
            
            repX, repY = findRep(x), findRep(y)

            if repX == repY:
                redundant = [x, y]
                return

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
            
            
        return redundant
