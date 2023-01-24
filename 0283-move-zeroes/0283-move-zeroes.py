class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for ind in range(len(nums)):
            if nums[ind]:
                nums[l], nums[ind] = nums[ind], nums[l]
                l += 1
            