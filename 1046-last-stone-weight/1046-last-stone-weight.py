class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x: -x, stones))
        heapify(heap)
        
        while len(heap) > 1:
            y = heappop(heap)
            x = heappop(heap)
            
            if y != x:
                heappush(heap, y-x)
                
        if not heap:
            return 0
        
        return -heap[0]