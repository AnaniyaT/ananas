class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {}
        rank = {}

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
            if x not in rep:
                rep[x] = x
                rank[x] = 1
            if y not in rep:
                rep[y] = y
                rank[y] = 1
                
            repX, repY = findRep(x), findRep(y)
            
            if repX == repY:
                return

            if rank[repX] >= rank[repY]:
                repX, repY = repY, repX

            rep[repX] = repY
            rank[repY] += rank[repX]

        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        def isValid(r, c):
            return 1 <= r <= row and 1 <= c <= col
        
        left, right = (-1, -1), (-2, -2)
        union(left, left)
        union(right, right)
        
        step = 0
        for r, c in cells:
            union((r, c), (r, c))
            if c == 1:
                union(left, (r, c))
            if c == col:
                union(right, (r, c))
                
            for rOff in [-1, 0, 1]:
                for cOff in [-1, 0, 1]:
                    newR, newC = r + rOff, c + cOff
                    if isValid(newR, newC) and (newR, newC) in rep:
                        union((r, c), (newR, newC))
                            
            if isConnected(left, right):
                return step
            
            
            step += 1
            
        
        
                        