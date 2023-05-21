class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            
        visited = set()
        def dfs(node):
            summ = 0
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    summ += dfs(neigh)
                    
            return summ + 1 if summ else int(hasApple[node])
        
        visited.add(0)
        ans = 2 * dfs(0)
        
        return ans - 2 if ans else 0