class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {chr(x): chr(x) for x in range(ord("a"), ord("z") + 1)}
        rank = {chr(x): 1 for x in range(ord("a"), ord("z") + 1)}
        minChr = {chr(x): chr(x) for x in range(ord("a"), ord("z") + 1)}

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
            minChr[repY] = min(minChr[repY], minChr[repX])

        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        for ind in range(len(s1)):
            union(s1[ind], s2[ind])
            
        res = []
        for ch in baseStr:
            res.append(minChr[findRep(ch)])
            
        return "".join(res)