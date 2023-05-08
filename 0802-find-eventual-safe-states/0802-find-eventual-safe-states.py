class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = []
        colors = ["w" for _ in range(len(graph))]
        
        def ts(node):
            if colors[node] == "b":
                return True
            
            if colors[node] == "g":
                return False
            
            colors[node] = "g"
            
            for neigh in graph[node]:
                if not ts(neigh):
                    return False
            
            colors[node] = "b"
            safe.append(node)
            
            return True
        
        for node in range(len(graph)):
            if colors[node] == "w":
                ts(node)
                
        return sorted(safe)