class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for fro, to in adjacentPairs:
            graph[fro].append(to)
            graph[to].append(fro)
            indeg[fro] += 1
            indeg[to] += 1
            
        visited = set()
        queue = deque()
        for key in indeg:
            if indeg[key] == 1:
                queue.append(key)
                visited.add(key)
                break
                
        ans = []
        
        
        while queue:
            cur = queue.pop()

            ans.append(cur)
            for neigh in graph[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.appendleft(neigh)
                
        return ans