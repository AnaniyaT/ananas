class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def findDivisionSum(n):
            summ = 0
            
            for num in nums:
                summ += ceil(num / n)
                
            return summ
        
        start, end = 1, max(nums)
        
        while start <= end:
            
            mid = start + (end - start) // 2
            divisionSum = findDivisionSum(mid)
            
            if divisionSum <= threshold:
                end = mid - 1
            else:
                start = mid + 1
                
        return start