class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        answer = []
        
        def backtrack(subset, ind):
            nonlocal length
            
            if ind == length:
                answer.append(subset[:])
                return
                
            subset.append(nums[ind])
            
            backtrack(subset, ind + 1)
            
            subset.pop()
            
            backtrack(subset, ind + 1)
            
        backtrack([], 0)
        
        return answer