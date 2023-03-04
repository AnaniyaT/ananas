class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        # finding left most index
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        start = l
        
        l, r = 0, len(nums) - 1
        
        
        # finding right most index
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
                
        end = r
        
        # if the element doesn't exist
        if start > end:
            return [-1, -1]
        
        return [start, end]
                
        