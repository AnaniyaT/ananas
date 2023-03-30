class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for ind in range(len(nums)):
            
            while nums[ind] != ind + 1 and nums[nums[ind] - 1] != nums[ind]:
                num = nums[ind] 
                nums[ind], nums[num - 1] = nums[num -1], nums[ind]
                
        for ind, num in enumerate(nums):
            if ind != num -1:
                duplicates.append(num)
                
        return duplicates