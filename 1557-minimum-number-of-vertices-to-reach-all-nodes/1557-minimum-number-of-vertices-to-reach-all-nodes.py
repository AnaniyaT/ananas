class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for fro, to in edges:
            graph[fro].append(to)
            graph[to]
            
        needed = set()
        visited = set()
        
        def dfs(node):
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour in needed:
                    needed.remove(neighbour)
                
                if neighbour not in visited:
                    dfs(neighbour)
                    
        for node in graph:
            if node not in visited:
                needed.add(node)
                dfs(node)
                
        return list(needed)