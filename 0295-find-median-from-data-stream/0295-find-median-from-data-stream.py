
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        while len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
            
        while len(self.left) - 1 > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()