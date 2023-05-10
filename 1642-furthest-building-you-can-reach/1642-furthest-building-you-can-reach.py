class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        bIdx = 0
        
        for ind in range(1, len(heights)):
            if heights[ind] <= heights[ind - 1]:
                bIdx += 1
                continue
                
            heappush(heap, heights[ind] - heights[ind-1])
            
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
            if bricks >= 0:
                bIdx += 1
            else:
                break
                
                    
        return bIdx
            