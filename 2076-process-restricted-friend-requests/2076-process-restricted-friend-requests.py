class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
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

            
        def isPossible(fro, to):
            reps = [findRep(fro), findRep(to)]
            
            for fr, t in restrictions:
                if findRep(fr) in reps and findRep(t) in reps:
                    return False
            
            return True
        
        
        ans = []
        
        for fro, to in requests:
            if isPossible(fro, to):
                ans.append(True)
                union(fro, to)
            else:
                ans.append(False)
                
        return ans
            
        