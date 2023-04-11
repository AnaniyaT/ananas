class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for fro, to in roads:
            graph[fro].add(to)
            graph[to].add(fro)
            
        maxRank = 0
        
        sortedRank = list(graph.keys())
        # print(graph)
        for ind in range(len(sortedRank)):
            for ind1 in range(ind + 1, len(sortedRank)):
                rank = len(graph[sortedRank[ind]]) + len(graph[sortedRank[ind1]])
                if sortedRank[ind] in graph[sortedRank[ind1]]:
                    rank -= 1
                
                maxRank = max(maxRank, rank)
            
        return maxRank