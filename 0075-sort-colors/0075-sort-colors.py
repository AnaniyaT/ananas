class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countArr = [0,0,0]
        for num in nums:
            countArr[num] += 1
        p = 0
        for ind in range(3):
            for _ in range(countArr[ind]):
                nums[p] = ind
                p += 1
                
        