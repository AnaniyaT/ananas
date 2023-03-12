class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        summ = 0
        
        def backtrack(temp, ind):
            nonlocal summ
            
            if ind == len(nums):
                summ += temp
                return
            
            num = nums[ind]
            temp ^= num
            
            backtrack(temp, ind + 1)
            
            temp ^= num
            
            backtrack(temp, ind + 1)
            
        backtrack(0, 0)
        
        return summ
            