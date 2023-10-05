class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        
        for edge, (fro, to) in enumerate(edges):
            graph[fro].append((to, succProb[edge]))
            graph[to].append((fro, succProb[edge]))
        
        visited = [0 for _ in range(n)]
        queue = [(-1, start_node)]
        
        while queue:
            # print(queue)
            prob, node = heappop(queue)
            
            visited[node] = 1
            
            if node == end_node:
                return -prob
            
            for neigh, probs in graph[node]:
                if not visited[neigh]:
                    heappush(queue, (prob * probs, neigh))
                    
        return 0