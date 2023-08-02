class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        rep = [i for i in range(n)]
        rank = [[source[i]] for i in range(n)]
        tRank = [[target[i]] for i in range(n)]

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
            tRank[repY].extend(tRank[repX])
            tRank[repX] = []

        def difference(arr1, arr2):
            counts1 = Counter(arr1)
            counts2 = Counter(arr2)
            
            diff = 0
            for key in counts1:
                if key in counts2:
                    diff += max(0, counts1[key] - counts2[key])
                else:
                    diff += counts1[key]
                    
            return diff
        
        for fro, to in allowedSwaps:
            union(fro, to)
            
        hamDist = 0
        for ind in range(n):
            hamDist += difference(rank[ind], tRank[ind])
            
        # print(tRank)
        # print(rank)
        return hamDist
        
        