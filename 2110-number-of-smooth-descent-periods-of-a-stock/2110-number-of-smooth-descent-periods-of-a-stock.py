class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = count = 0
        for r, i in enumerate(prices):
            if r!=l:
                if i+1 != prices[r-1]:
                    n = r-l
                    count += int(((n-1)*n)/2)
                    l = r
        if l != len(prices)-1:
            n = r-l
            print(r)
            count += int(((n+1)*n)/2)
        return count + len(prices)