class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            indeg[fro] += 1
            indeg[to] += 1
            
        queue = deque()
        
        for node in range(n):
            if indeg[node] <= 1:
                queue.append(node)
                indeg[node] -= 1
        
        while queue:
            size = len(queue)
            last = []
            for _ in range(size):
                cur = queue.pop()
                last.append(cur)
                for neigh in graph[cur]:
                    indeg[neigh] -= 1
                    if indeg[neigh] == 1:
                        queue.appendleft(neigh)
                        indeg[neigh] = 0
                        
        return last
                    