class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        
        for child in range(len(parent)):
            tree[parent[child]].append(child)
            
        maxPathLen = 0
        
        def dfs(node, parent):
            nonlocal maxPathLen
            
            results = [0]
            for child in tree[node]:
                results.append(dfs(child, s[node]))
                
            maxPathLen = max(maxPathLen, sum(sorted(results, reverse=True)[:2]) + 1)
            
            if s[node] == parent:
                return 0
            
            return max(results) + 1
        
        dfs(0, "A")
        
        return maxPathLen
        
            
                
            