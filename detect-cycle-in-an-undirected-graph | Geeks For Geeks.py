# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		colors = ['w' for _ in range(V)]
		
		def dfs(par, n):
		    if colors[n] == 'b':
                return False
		    if colors[n] == 'g':
		        return True
            
            colors[n] = 'g'
            for neigh in adj[n]:
                if neigh != par and dfs(n, neigh):
                    return True
                    
            colors[n] = 'b'
            return False
            
        for ind in range(V):
            if dfs(-1, ind):
                return True
                
        return False
