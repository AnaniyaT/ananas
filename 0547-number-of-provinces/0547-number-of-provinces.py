class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        length = len(isConnected)
        provinces = 0
        
        def dfs(fro):
            nonlocal length
            
            visited.add(fro)
            
            for to in range(length):
                if isConnected[fro][to] and to not in visited:
                    dfs(to)
        
        for fro in range(length):
            if fro in visited:
                continue
        
            provinces += 1
            dfs(fro)
            
        return provinces
            
                