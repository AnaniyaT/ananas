class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg = [0 for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        for fro, to in relations:
            graph[fro-1].append(to-1)
            indeg[to-1] += 1
        
        queue = deque()
        times = [-float('inf') for _ in range(n)]
        for node in range(n):
            if not indeg[node]:
                queue.append(node)
                times[node] = time[node]
        
        while queue:
            cur = queue.pop()
            
            for child in graph[cur]:
                indeg[child] -= 1
                times[child] = max(times[child], times[cur] + time[child])
                if not indeg[child]:
                    queue.appendleft(child)
                    
        return max(times)