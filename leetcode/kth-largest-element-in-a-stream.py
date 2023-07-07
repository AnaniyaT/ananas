class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)

        while len(self.heap) > k:
            heappop(self.heap)
            
        while len(self.heap) < k:
            heappush(self.heap, -float('inf'))

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)