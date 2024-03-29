class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        for i in range(len(nums)//2):
            nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range((len(nums)-k)//2):
            nums[i+k], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i+k]
            