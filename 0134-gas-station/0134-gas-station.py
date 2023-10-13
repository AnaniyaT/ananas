class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diffs = [gas[i] - cost[i] for i in range(n)]
        
        if sum(diffs) < 0:
            return -1
        
        ans = -1
        pre = 0
        for idx in range(n):
            if diffs[idx] >= 0 and ans == -1:
                ans = idx
                
            pre += diffs[idx]
            if pre < 0:
                ans = -1
                pre = 0
                
        return ans