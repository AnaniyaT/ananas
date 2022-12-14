class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        maxx = 0
        for ind in range(len(nums)):
            if ind - 2 >= 0:
                maxx = max(maxx, nums[ind-2])
                nums[ind] += maxx
        return max(nums[-1],nums[-2])