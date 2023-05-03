from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length % 2:
            return float(self.nums[length // 2])
        else:
            return (self.nums[length // 2] + self.nums[(length // 2) - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()