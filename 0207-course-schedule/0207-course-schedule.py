class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = defaultdict(lambda: "w")
        
        for then, first in prerequisites:
            graph[first].append(then)
            
        def ts(node):
            if colors[node] == "g":
                return False
            
            if colors[node] == "b":
                return True
            
            colors[node] = "g"
            
            for neigh in graph[node]:
                if not ts(neigh):
                    return False
                
            colors[node] = "b"
            
            return True
        
        for node in range(numCourses):
            if not ts(node):
                return False
            
        return True