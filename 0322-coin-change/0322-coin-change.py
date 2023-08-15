class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def rec(coin):
            if coin in cache:
                return cache[coin]
            
            if not coin:
                return 0
            
            if coin < 0:
                return float('inf')
            
            results = []
            for num in coins:
                res = rec(coin - num)
                results.append(res + 1)
                
            cache[coin] = min(results)
            return cache[coin]
        
        ans = rec(amount)
        return ans if ans != float('inf') else -1