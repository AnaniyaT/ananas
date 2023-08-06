class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return n
        
        nums = [0, 1]
        maxx = 1
        
        for num in range(2, n + 1):
            if not num % 2:
                nums.append(nums[num//2])
            else:
                nums.append(nums[num//2] + nums[num//2 + 1])
                
            maxx = max(maxx, nums[num])
            
        return maxx