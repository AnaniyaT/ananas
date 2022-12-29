class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        product = 1
        subarrays = 0
        
        while j < len(nums):
            if product * nums[j] < k:
                product *= nums[j]
                j += 1
                subarrays += j - i
            elif i < j:
                product //= nums[i]
                i += 1
            else:
                i += 1
                j += 1
                
        return subarrays
            