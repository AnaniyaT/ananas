class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
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

            if repX == repY:
                return

            if rank[repX] >= rank[repY]:
                repX, repY = repY, repX

            rep[repX] = repY
            rank[repY] += rank[repX]

        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        edgeIndx = sorted([ind for ind in range(len(edgeList))], key=lambda x: edgeList[x][2])
        queryIndx = sorted([ind for ind in range(len(queries))], key=lambda x: queries[x][2])
        
        ans = [False for _ in range(len(queries))]
        
        ind = 0
        
        for queryInd in queryIndx:
            fro, to, dist = queries[queryInd]
            
            while ind < len(edgeList) and dist > edgeList[edgeIndx[ind]][2] and not isConnected(fro, to):
                fr, t, _ = edgeList[edgeIndx[ind]]
                union(fr, t)
                ind += 1
                
            if isConnected(fro, to):
                ans[queryInd] = True
                
        return ans
                
        
        