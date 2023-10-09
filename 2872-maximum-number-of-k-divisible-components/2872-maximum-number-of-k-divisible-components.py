class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            
        components = 0
        
        visited = [0 for _ in range(n)]
        def dfs(node):
            nonlocal components
            visited[node] = 1
            neighbours = [0]
            for neigh in graph[node]:
                if not visited[neigh]:
                    neighbours.append(dfs(neigh))
             
            summ = sum(neighbours) + values[node]
            summ %= k
            if not summ:
                components += 1
            
            return summ
        
        dfs(0)
        return components