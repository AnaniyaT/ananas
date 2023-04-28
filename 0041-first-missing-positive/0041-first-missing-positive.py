class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        for ind in range(length):
            while nums[ind] != ind + 1 and not (nums[ind] > length or nums[ind] <= 0 or nums[nums[ind] -1] == nums[ind]):
                num = nums[ind]
                nums[ind], nums[num-1] = nums[num-1], nums[ind]
                
        for ind in range(length):
            if nums[ind] != ind + 1:
                return ind + 1
            
        return length + 1