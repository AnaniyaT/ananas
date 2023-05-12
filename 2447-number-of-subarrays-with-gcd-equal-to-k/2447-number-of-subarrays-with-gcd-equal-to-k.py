class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        subArrays = 0
        
        for i in range(len(nums)):
            gcd_ = 0
            for j in range(i, len(nums)):
                gcd_ = gcd(gcd_, nums[j])
                
                if gcd_ == k:
                    subArrays += 1
                    
        return subArrays