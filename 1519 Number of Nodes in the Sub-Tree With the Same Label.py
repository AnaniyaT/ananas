class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            
        ans = [0 for _ in range(n)]
        
        def dfs(p, n):
            label = labels[n]
            counts = defaultdict(int)
            
            counts[label] += 1
            
            for neigh in graph[n]:
                if neigh != p:
                    incomingCounts = dfs(n, neigh)
                    for lett in incomingCounts:
                        counts[lett] += incomingCounts[lett]
            
            ans[n] = counts[label]
            return counts
        
        dfs(-1, 0)
        
        return ans
