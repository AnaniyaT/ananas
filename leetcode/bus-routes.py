class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        
        for bus in range(len(routes)):
            for stop in routes[bus]:
                graph[-bus-1].append(stop)
                graph[stop].append(-bus-1)
            
        visited = set([source])
        queue = deque([source])
        step = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop()
                if cur == target:
                    print(step)
                    print(cur)
                    return step // 2
                
                for neigh in graph[cur]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.appendleft(neigh)
                    
            step += 1
                         
        
        return -1
        
        
                         
        