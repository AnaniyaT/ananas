class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for fro, to in roads:
            graph[fro].append(to)
            graph[to].append(fro)
            
        maxRank = 0
        
        sortedRank = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
        
        for ind in range(len(sortedRank)):
            for ind1 in range(ind + 1, len(sortedRank)):
                rank = len(graph[sortedRank[ind]]) + len(graph[sortedRank[ind1]])
                if sortedRank[ind] in graph[sortedRank[ind1]]:
                    rank -= 1
                    
                # if rank < maxRank:
                #     return maxRank
                
                maxRank = max(maxRank, rank)
            
        return maxRank