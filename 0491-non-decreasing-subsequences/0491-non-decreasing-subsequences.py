class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subSequences = set()
        answer = []
        curr = []
        length = len(nums)
        
        def backtrack(ind):
            nonlocal length
            
            if ind == length:
                if len(curr) > 1 and tuple(curr) not in subSequences:
                    subSequences.add(tuple(curr))
                    answer.append(curr[:])
                    
                return
            
            num = nums[ind]
            if not curr or curr[-1] <= num:
                curr.append(num)
                backtrack(ind + 1)
                curr.pop()
                
            backtrack(ind + 1)
            
        backtrack(0)
        
        return answer
            
            
            