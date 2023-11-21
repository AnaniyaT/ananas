class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        times = [0 for _ in range(n)]
        time = 0
        
        for idx in range(1, n):
            times[idx] += times[idx-1] + travel[idx-1]
            
        last = [0, 0, 0]
            
        for idx in range(n):
            time += len(garbage[idx])
            if "G" in garbage[idx]:
                last[0] = idx
            if "P" in garbage[idx]:
                last[1] = idx
            if "M" in garbage[idx]:
                last[2] = idx
            
        for lastIdx in last:
            time += times[lastIdx]
            
        return time