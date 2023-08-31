class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for fro, to, cost in edges:
            self.graph[fro].append((to, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        minCost = float('inf')
        visited = set()
        while queue:
            cost, cur = heappop(queue)
            visited.add(cur)
            
            if cur == node2:
                return cost
            
            for neigh, c in self.graph[cur]:
                if neigh not in visited:
                    heappush(queue, (cost + c, neigh))
                    
        return -1
        
        return minCosts[node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)