class Solution:
    def __init__(self):
        self.pivot = 0
        
    def compare(self, num):
        if num == self.pivot:
            return 0
        if num < self.pivot:
            return -1
        else:
            return 1
        
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        self.pivot = pivot
        return sorted(nums, key=self.compare)