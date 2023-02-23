class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = nums
        self.sum.append(0)
        for ind in range(len(nums)-1):
            self.sum[ind] += self.sum[ind-1]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right] - self.sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)