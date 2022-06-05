class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        j = len(nums)-1
        i =0
        count = 0
        while j>i:
            if nums[i]+nums[j] == k:
                count +=1
                del nums[j]
                del nums[i]
                j-=2
            elif nums[i]+nums[j] < k:
                i+=1
            else:
                j-=1
        return count