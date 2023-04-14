class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Build the adjacency list
        adjacency = defaultdict(list)
        for node, edges in enumerate(graph):
            for to in edges:
                adjacency[node].append(to)
        
        # list to store all found paths and list to keep track of current path
        paths = []
        currPath = []
        
        def dfs(curr, dest):
            currPath.append(curr)
            if curr == dest:
                paths.append(currPath[:])
            
            for edge in adjacency[curr]:
                dfs(edge, dest)
                currPath.pop()
                
                
        dfs(0, len(graph) - 1)
        
        return paths