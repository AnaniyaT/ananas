class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        triplets = 0
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                triplets += bisect_left(nums, nums[i] + nums[j], j+1, n) - j - 1
                
        return triplets