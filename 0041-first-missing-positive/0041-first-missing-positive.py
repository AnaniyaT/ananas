class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        for ind in range(length):
            if nums[ind] <= 0:
                nums[ind] = length + 1
                
        for ind in range(length):
            num = abs(nums[ind])
            if num <= length and nums[num-1] > 0:
                nums[num-1] *= -1
                
        for ind in range(length):
            if nums[ind] > 0:
                return ind + 1
            
        return length + 1