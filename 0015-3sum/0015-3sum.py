class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)
        
        for i in range(n-2):
            l, r = i + 1, n - 1
            
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot < 0:
                    l += 1
                elif tot > 0:
                    r -= 1
                else:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    
        return list(map(list, triplets))