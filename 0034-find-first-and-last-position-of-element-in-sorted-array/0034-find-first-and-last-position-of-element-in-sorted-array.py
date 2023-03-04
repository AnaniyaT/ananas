class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        start = l
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
                
        end = r
        
        if start > end:
            return [-1, -1]
        
        return [start, end]
                
        