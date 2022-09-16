class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,summ = 0,0,0
        maxx = 0
        flipped = 0
        while r < len(nums):
            if nums[r] == 0 and flipped == k:
                if nums[l] == 0:
                    flipped -= 1
                summ -= 1
                l += 1
            elif nums[r] == 0:
                r += 1 
                flipped += 1
                summ += 1
                maxx = max(maxx, summ)
            else:
                r += 1
                summ += 1
                maxx = max(maxx, summ)
        return maxx