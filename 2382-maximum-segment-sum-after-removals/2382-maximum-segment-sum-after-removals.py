class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        rep = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]

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

        sums = [0 for _ in range(n+1)]
        maxx = 0
        ans = [0 for _ in range(n)]
        
        for ind, rem in enumerate(reversed(removeQueries[1:])):
            tot = nums[rem]
            for add in [-1, 1]:
                if sums[findRep(rem+add)]:
                    halfSum = sums[findRep(rem+add)]
                    union(rem+add, rem)
                    tot += halfSum
            
            sums[findRep(rem)] = tot
            maxx = max(maxx, tot)
            ans[n-ind-2] = maxx
            
        return ans
            
                
            