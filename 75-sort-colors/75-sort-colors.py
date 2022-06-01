class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0,0,0]
        for i in nums:
            arr[i]+=1
        ind = 0
        for l in range (0,3):
            for j in range (0,arr[l]):
                nums[ind] = l
                ind+=1