class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missNum = -1
        
        for ind in range(len(nums)):
            
            while nums[ind] != ind + 1:
                num = nums[ind]
                if not num:
                    missNum = ind
                    break
                    
                nums[ind], nums[num - 1] = nums[num - 1], nums[ind]
                
        return missNum + 1
