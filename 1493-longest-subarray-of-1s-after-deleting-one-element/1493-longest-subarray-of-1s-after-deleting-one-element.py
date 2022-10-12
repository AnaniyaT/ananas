class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count0 = l = 0
        
        for r, i in enumerate(nums):
            if count0 > 1:
                if nums[l] == 0:
                    count0 -= 1
                l += 1
            if i == 0:
                count0 += 1
        if count0 > 1:
            return r-l-1
        else:
            return r-l