class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        count = 0
        curr = 0
        length = len(nums)
        
        def backtrack(ind):
            nonlocal maxOr, count, curr, length
            
            if ind == length:
                return
            
            before = curr
            curr |= nums[ind]
            
            if curr == maxOr:
                count += 1
            elif curr > maxOr:
                count = 1
                maxOr = curr
                
            backtrack(ind + 1)
            curr = before
            
            backtrack(ind + 1)
            
        backtrack(0)
        
        return count
            