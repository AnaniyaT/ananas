class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        k=1
        while k<len(nums):
            i = 0
            while i <len(nums)-1:
                if int(nums[i]+nums[i+1])<int(nums[i+1]+nums[i]): nums[i],nums[i+1]= nums[i+1],nums[i]
                i+=1
            k+=1
        return str(int("".join(nums)))
            
        