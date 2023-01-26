class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind-1]:
                nums[p] = nums[ind]
                p += 1
        
        return p