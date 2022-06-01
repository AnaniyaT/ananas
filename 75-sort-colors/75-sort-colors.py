class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n0 = 0
        n1 = 0
        n2 = 0
        for i in nums:
            if i == 0: n0 += 1
            elif i == 1: n1 += 1
            elif i == 2: n2 += 1
        k = 0
        for i in range (0,n0):
            nums[k] = 0
            k+=1
        for i in range (0,n1):
            nums[k] = 1
            k+=1
        for i in range (0,n2):
            nums[k] = 2
            k+=1