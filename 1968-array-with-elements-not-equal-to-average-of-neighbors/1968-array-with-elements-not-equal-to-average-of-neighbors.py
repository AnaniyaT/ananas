class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        lst = [0]*len(nums)
        even = 0
        odd = 1
        for i in nums[:len(nums)//2]:
            lst[odd] = i
            odd+=2
        for i in nums[len(nums)//2:]:
            lst[even] = i
            even+=2
        return lst
            