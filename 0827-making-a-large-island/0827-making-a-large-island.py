class Rep(defaultdict):
    def __missing__(self, key):
        return key

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rep = Rep()
        rank = defaultdict(lambda : 1)

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
        
        n = len(grid)
        m = len(grid[0])
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < m and grid[r][c]
        
        maxSize = 0
        for r in range(n):
            for c in range(m):
                up = (r-1, c)
                left = (r, c-1)
                
                if not isValid(r, c):
                    continue
                
                if isValid(*up):
                    union((r, c), up)
                if isValid(*left):
                    union((r, c), left)
                    
                maxSize = max(maxSize, rank[findRep((r, c))])
                    
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    continue
                
                visited = set()
                neighs = 0
                for ro, co in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = r + ro, c + co
                    if isValid(nr, nc):
                        rp = findRep((nr, nc))
                        if rp not in visited:
                            neighs += rank[rp]
                            visited.add(rp)
                            
                maxSize = max(maxSize, neighs + 1)
        
        return maxSize