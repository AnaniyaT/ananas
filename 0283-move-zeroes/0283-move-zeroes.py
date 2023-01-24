class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for ind in range(len(nums)):
            if (not nums[l]) and nums[ind]:
                nums[l], nums[ind] = nums[ind], nums[l]
                
            if nums[l]:
                l += 1