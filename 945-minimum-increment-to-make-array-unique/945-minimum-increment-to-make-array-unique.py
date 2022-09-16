class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        prevmax = -1
        increments = 0
        for i in sorted(nums):
            if prevmax < i:
                prevmax = i
            else:
                increments += (prevmax-i)+1
                prevmax += 1
        return increments