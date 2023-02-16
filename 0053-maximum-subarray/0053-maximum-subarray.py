class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        minn = 0
        maxx = -float("inf")
        for num in nums:
            pre += num
            maxx = max(maxx, (pre-minn))
            minn = min(minn, pre)
            
        return maxx