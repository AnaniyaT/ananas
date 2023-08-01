class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for ind in range(2, len(cost)):
            cost[ind] += min(cost[ind-1], cost[ind-2])
            
        return min(cost[-1], cost[-2])