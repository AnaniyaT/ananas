class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        frwrd = 1
        revrs = 1
        
        for ind in range(len(nums)):
            answer[ind] *= frwrd
            answer[~ind] *= revrs
            frwrd *= nums[ind]
            revrs *= nums[~ind]
            
        return answer