class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        rep = [i for i in range(n)]
        letters = [[ch] for ch in s]

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

            if len(letters[repX]) >= len(letters[repY]):
                repX, repY = repY, repX

            rep[repX] = repY
            letters[repY].extend(letters[repX])
            letters[repX] = []

        def isConnected(x, y):
            return findRep(x) == findRep(y)
        
        for fro, to in pairs:
            union(fro, to)
            
        for arr in letters:
            arr.sort(reverse=True)
            
        ans =[]
        for ind in range(n):
            ans.append(letters[findRep(ind)].pop())
            
        return "".join(ans)
        
        