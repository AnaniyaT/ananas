class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minBefore = [float('inf')]
        for num in nums[:len(nums)-1]:
            minBefore.append(min(minBefore[-1], num))
            
        stack = []
        for ind in range(len(nums)):
            num = nums[~ind]
            while stack and stack[-1] < num:
                if stack[-1] > minBefore[~ind]:
                    return True
                stack.pop()
                
            stack.append(nums[~ind])
                
        return False
            
            