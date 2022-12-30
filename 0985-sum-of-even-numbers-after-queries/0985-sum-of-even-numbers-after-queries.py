class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in nums:
            if num%2 == 0:
                evenSum += num
                
        result = []
        
        for query in queries:
            val = query[0]
            ind = query[1]
            if nums[ind] % 2 == 0:
                if val % 2 == 0:
                    evenSum += val
                else:
                    evenSum -= nums[ind]
            else:
                if val % 2 != 0:
                    evenSum += val + nums[ind]
            
            nums[ind] += val
            
            result.append(evenSum)
            
        return result
