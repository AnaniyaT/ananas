class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [-1] * length
        
        stack = []
        for ind in range(2*length):
            num = nums[ind%length]
            
            while stack and nums[stack[-1]] < num:
                answer[stack[-1]] = num
                stack.pop()
                
            stack.append(ind%length)
            
        return answer