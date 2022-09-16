class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = list(nums)
        for i,j in enumerate(temp):
            nums[(i+k)%len(nums)] = j