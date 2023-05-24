class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        
        costs.sort(key=lambda x: x[0] - x[1])
        
        cost = 0
        for a, b in costs[:n]:
            cost += a
        
        for a, b in costs[n:]:
            cost += b
            
        return cost