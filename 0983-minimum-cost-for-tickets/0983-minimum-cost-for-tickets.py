class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        @cache
        def dfs(ind):
            if ind >= n:
                return 0
            
            cur = days[ind]
            
            one = dfs(ind + 1) + costs[0]
            
            i = ind
            while i < n and days[i] - cur < 7:
                i += 1
                
            seven = dfs(i) + costs[1]
            
            i = ind
            while i < n and days[i] - cur < 30:
                i += 1
                
            thirty = dfs(i) + costs[2]
            
            return min(one, seven, thirty)
        
        return dfs(0)