class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x, y = stones[i]
            for j in range(i+1, n):
                x1, y1 = stones[j]
                if x == x1 or y == y1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        left = 0
        for ind in range(n):
            if ind not in visited:
                left += 1
                dfs(ind)
                
        return n - left
            
            