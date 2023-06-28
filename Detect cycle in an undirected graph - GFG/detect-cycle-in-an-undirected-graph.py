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


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends