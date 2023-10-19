class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = 26
        
        def toNum(lett):
            return ord(lett) - ord("a")
        
        def toLett(num):
            return chr(ord("a") + num)
        
        rep = [i for i in range(n)]
        rank = [[i] for i in range(n)]

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

            if len(rank[repX]) >= len(rank[repY]):
                repX, repY = repY, repX

            rep[repX] = repY
            rank[repY].extend(rank[repX])
            rank[repX] = []

        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        for ind in range(len(s1)):
            i1 = toNum(s1[ind])
            i2 = toNum(s2[ind])
            
            union(i1, i2)
        for r in rank:
            r.sort()
            
        newS = []
        for lett in baseStr:
            r = findRep(toNum(lett))
            smLett = rank[r][0]
            
            newS.append(toLett(smLett))
            
        return "".join(newS)
