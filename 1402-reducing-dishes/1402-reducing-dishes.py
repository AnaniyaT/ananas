class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        nums = 0
        total = 0
        
        for num in satisfaction:
            nums += num
            if nums < 0:
                break
            
            total += nums
                
        return total