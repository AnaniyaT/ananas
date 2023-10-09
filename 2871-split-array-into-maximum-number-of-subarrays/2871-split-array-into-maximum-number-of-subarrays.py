class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        a = nums[0]
        subs = 1
        
        for num in nums[1:]:
            if not a:
                subs += 1
                a = num
            else:
                a &= num
                
        if a and subs > 1:
            subs -= 1
            
        return subs