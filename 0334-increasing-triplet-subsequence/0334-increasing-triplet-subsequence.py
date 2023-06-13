class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        idk = [0 for _ in range(len(nums))]
        
        minn = float('inf')
        for ind in range(len(nums)):
            if nums[ind] > minn:
                idk[ind] += 1
            else:
                minn = nums[ind]
                
        maxx = -float('inf')
        for ind in range(len(nums)):
            if nums[~ind] < maxx:
                if idk[~ind]:
                    return True
            
            else:
                maxx = nums[~ind]
                
        return False