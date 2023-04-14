class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for bomb, (x, y, r) in enumerate(bombs):
            for bomb1, (x1, y1, r1) in enumerate(bombs):
                distanceSq = (x - x1) ** 2 + (y - y1) ** 2
                
                if bomb != bomb1 and r ** 2 >= distanceSq:
                    graph[bomb].append(bomb1)
        
        
        def dfs(node, visited):
            visited.add(node)
            visitedNodes = 1
            for to in graph[node]:
                if to not in visited:
                    visitedNodes += dfs(to, visited)
                    
            return visitedNodes
        
        maxPathLen = 0
        for node in range(len(bombs)):
            maxPathLen = max(maxPathLen, dfs(node, set()))
            
        return maxPathLen