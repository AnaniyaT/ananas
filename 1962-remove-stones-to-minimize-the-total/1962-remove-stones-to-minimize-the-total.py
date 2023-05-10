class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -x, piles))
        
        heapify(piles)
        
        for _ in range(k):
            big = -heappop(piles)
            heappush(piles, -(big - (big // 2)))
            
        return -sum(piles)
            