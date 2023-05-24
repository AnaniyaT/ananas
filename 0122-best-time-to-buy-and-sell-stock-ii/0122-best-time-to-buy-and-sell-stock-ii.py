class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = mn = prices[0]
        profit = 0
        
        for ind in range(1, len(prices)):
            if prices[ind] < prices[ind-1]:
                profit += mx - mn
                mx = mn = prices[ind]
            else:
                mx = max(mx, prices[ind])
                mn = min(mn, prices[ind])
                
        profit += mx-mn
        
        return profit