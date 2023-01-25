class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for ind in range(len(nums)-1):
            if nums[ind] == nums[ind+1]:
                nums[ind] *= 2
                nums[ind+1] = 0
                
        l = 0
        for r in range(len(nums)):
            nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
            
        return nums