class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pr = len(nums) -1
        pl = 0
        posans = 0
        for i in range (len(nums)//2):
            if posans < nums[pl]+nums[pr]:
                posans = nums[pl]+nums[pr]
                pl+=1
                pr-=1
            else:
                pl+=1
                pr-=1
        return posans
            