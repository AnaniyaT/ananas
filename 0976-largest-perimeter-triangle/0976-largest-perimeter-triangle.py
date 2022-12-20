class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for ind in range(len(nums)-1, 1, -1):
            longest = max(nums[ind], nums[ind-1], nums[ind-2])
            perimeter = sum(nums[ind-2:ind+1])
            if longest < perimeter - longest:
                return perimeter
        return 0