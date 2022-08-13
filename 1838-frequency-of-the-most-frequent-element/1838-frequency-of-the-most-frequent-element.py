class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        maxFreq,l,r,summ = 0,0,0,0
        while r < len(nums):
            size = r-l
            if (nums[r]*size)-summ <= k:
                maxFreq = max(maxFreq,size+1)
                summ += nums[r]
                r += 1
            else:
                summ -= nums[l]
                l += 1
        return maxFreq