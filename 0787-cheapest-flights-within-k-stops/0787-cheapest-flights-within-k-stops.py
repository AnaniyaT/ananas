class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        # print(n, len(flights))
        
        for fro, to, price in flights:
            # print(fro, to, price)
            graph[fro].append((to, price))
        
        heap = [(-1, 0, src)]
        visited = [float('inf') for _ in range(n)]
        
        while heap:
            kk, price, cur = heappop(heap)
            
            if kk > k or visited[cur] < price:
                continue
            
            visited[cur] = price
            
            for neigh, pr in graph[cur]:
                heappush(heap, (kk + 1 , price + pr, neigh))
         
        
        ans = visited[dst]
        
        return ans if ans != float('inf') else -1
        
        