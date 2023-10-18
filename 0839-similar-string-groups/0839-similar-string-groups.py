class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
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
        
        def areSimilar(s1, s2):
            l = len(s1)
            diff = 0
            for idx in range(l):
                if s1[idx] != s2[idx]:
                    diff += 1
                
                if diff > 2:
                    return False
                
            return True
        
        groups = n
        
        for idx in range(n):
            for idx2 in range(idx + 1, n):
                if areSimilar(strs[idx], strs[idx2]) and not isConnected(idx, idx2):
                    union(idx, idx2)
                    groups -= 1
                    
        return groups