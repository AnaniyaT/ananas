class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        numCount = 0
        greaterThan = 0
        for num in nums:
            if num < target:
                greaterThan += 1
            elif num == target:
                numCount += 1
                
        return [greaterThan+n for n in range(numCount)]
        
                
            
   