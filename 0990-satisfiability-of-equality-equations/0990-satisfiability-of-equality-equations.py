class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
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
        
        def ind(let):
            return ord(let) - ord('a')
        
        notEqual = []
        
        for equation in equations:
            let1, let2 = equation[0], equation[-1]
            if equation[1] == '=':
                union(ind(let1), ind(let2))
            else:
                notEqual.append((ind(let1), ind(let2)))
                
        for let1, let2 in notEqual:
            if isConnected(let1, let2):
                return False
            
        return True
        
        