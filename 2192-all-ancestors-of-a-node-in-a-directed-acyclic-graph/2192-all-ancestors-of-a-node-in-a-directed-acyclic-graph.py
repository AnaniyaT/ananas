class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        
        op = 0
        
        for fro, to in edges:
            graph[to].append(fro)
            
        def dfs(n, m):
            if m in visited:
                return
            
            visited.add(m)
            ans[n].append(m)
            for ch in graph[m]:
                dfs(n, ch)
            
        for ind in range(n):
            visited = set([ind])
            for ch in graph[ind]:
                dfs(ind, ch)
            
        for a in ans:
            a.sort()
            
        return ans