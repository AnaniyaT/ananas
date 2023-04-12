class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for fro, to in dislikes:
            graph[fro].append(to)
            graph[to].append(fro)
            
        colors = {}
        
        def dfs(p, clr=1):
            colors[p] = clr
            
            for hater in graph[p]:
                if hater not in colors:
                    if not dfs(hater, -1 * clr):
                        return False
                    
                elif colors[hater] == clr:
                    return False
                
            return True
        
        for person in graph:
            if person not in colors:
                if not dfs(person):
                    return False
                
        return True