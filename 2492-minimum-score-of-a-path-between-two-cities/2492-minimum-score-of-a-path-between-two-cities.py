class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]
        score = [float('inf') for _ in range(n + 1)]
        
        def findRep(x):
            cur = x
            while cur != rep[cur]:
                cur = rep[cur]
                
            while x != cur:
                prev = rep[x]
                rep[x] = cur
                x = prev
                
            return cur
                
        def union(x, y, cost):
            repX, repY = findRep(x), findRep(y)
            
            if rank[repX] < rank[repY]:
                rep[repX] = repY
                rank[repY] += rank[repX]
                score[repY] = min(score[repY], cost, score[repX])
            else:
                rep[repX] = repX
                rep[repY] = repX
                rank[repX] += rank[repY]
                score[repX] = min(score[repX], cost, score[repY])
                
        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        for fro, to, cost in roads:
            union(fro, to, cost)
            
        return score[findRep(1)]