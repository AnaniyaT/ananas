class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            num = nums[mid]
            
            if num > nums[r] and num >= nums[l]:
                l = mid + 1
                
            else:
                r = mid
                
        return nums[r]