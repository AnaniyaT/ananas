class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        for ind in range(length):
            while nums[ind] != ind + 1 and nums[nums[ind] - 1] != nums[ind]:
                num = nums[ind]
                nums[ind], nums[num - 1] = nums[num - 1], nums[ind]
             
        missing = []
        for ind, num in enumerate(nums):
            if num != ind +1:
                missing.append(ind + 1)
            
        return missing
            
                