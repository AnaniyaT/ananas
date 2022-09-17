class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        for i,j in enumerate(nums):
            if totalsum-leftsum-j == leftsum:
                return i
            leftsum += j
        return -1