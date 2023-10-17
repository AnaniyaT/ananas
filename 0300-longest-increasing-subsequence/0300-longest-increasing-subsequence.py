class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        greater = [1 for _ in range(n)]
        
        for idx in range(n-1, -1, -1):
            maxx = 0
            for indx in range(idx, n):
                if nums[indx] > nums[idx]:
                    maxx = max(maxx, greater[indx])
            
            greater[idx] += maxx
        
        # print(greater)
        return max(greater)
            