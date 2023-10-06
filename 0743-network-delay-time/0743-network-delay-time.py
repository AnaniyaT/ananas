class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for fro, to, time in times:
            graph[fro - 1].append((to - 1, time))
        
        inf = float('inf')
        times = [inf for _ in range(n)]
        queue = [(0, k-1)]
        
        while queue:
            time, cur = heappop(queue)
            
            times[cur] = min(times[cur], time)
            
            for neigh, timeAdd in graph[cur]:
                if time + timeAdd < times[neigh]:
                    heappush(queue, (time + timeAdd, neigh))
                    
        ans = max(times)
        # print(times)
        
        return ans if ans != inf else -1